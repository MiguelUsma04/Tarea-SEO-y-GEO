/*
 * GMarketing 2026-11 (v2) - Cloudflare Turnstile para los formularios de esta pagina.
 * - Pone una verificacion dentro de cada formulario (invisible salvo que Cloudflare pida un clic).
 * - Agrega la ficha ("cf_turnstile") a cada envio hacia los PHP de formularios; cada ficha se usa una sola vez.
 * - No modifica el codigo del sitio: intercepta fetch, XMLHttpRequest (jQuery) y el envio normal de formularios.
 */
(function () {
  'use strict';
  var SITEKEY = '0x4AAAAAAF85d85P_kSu7tTG';
  var DESTINOS = /(^|\/)(enviarwspp)\.php$/i;
  var ESPERA_MAX_MS = 90000;
  var widgets = [];          // { form, caja, id, ficha }
  var ultimoForm = null;

  function esDestino(url) {
    try { var u = new URL(url, window.location.href); return u.origin === window.location.origin && DESTINOS.test(u.pathname); } catch (e) { return false; }
  }
  function widgetDe(form) {
    for (var i = 0; i < widgets.length; i++) { if (widgets[i].form === form) { return widgets[i]; } }
    return null;
  }
  function tomarFicha(form) {
    var w = widgetDe(form);
    var candidatos = (w && w.ficha) ? [w] : widgets.filter(function (x) { return !!x.ficha; });
    if (!candidatos.length) { return ''; }
    var elegido = candidatos[0];
    var t = elegido.ficha;
    elegido.ficha = '';
    setTimeout(function () { try { window.turnstile.reset(elegido.id); } catch (e) {} }, 50);
    return t;
  }
  function avisar(form, mostrar) {
    var w = widgetDe(form) || widgets[0];
    if (!w) { return; }
    var aviso = w.caja.querySelector('.gm-ts-aviso');
    if (mostrar) {
      if (!aviso) {
        aviso = document.createElement('div');
        aviso.className = 'gm-ts-aviso';
        aviso.style.cssText = 'font:14px/1.3 sans-serif;color:#b45309;margin:6px 0;';
        aviso.textContent = 'Confirma la verificacion de seguridad para enviar tus datos.';
        w.caja.appendChild(aviso);
      }
      try { w.caja.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (e) {}
    } else if (aviso) { aviso.parentNode.removeChild(aviso); }
  }
  function esperarFicha(form, cb) {
    var inicio = Date.now(), avisado = false;
    (function mirar() {
      var t = tomarFicha(form);
      if (t) { if (avisado) { avisar(form, false); } cb(t); return; }
      if (!avisado && Date.now() - inicio > 2500) { avisado = true; avisar(form, true); }
      if (Date.now() - inicio > ESPERA_MAX_MS) { avisar(form, false); cb(''); return; }
      setTimeout(mirar, 200);
    })();
  }
  function agregar(body, t) {
    if (!t) { return body; }
    if (typeof FormData !== 'undefined' && body instanceof FormData) { body.set('cf_turnstile', t); return body; }
    if (typeof URLSearchParams !== 'undefined' && body instanceof URLSearchParams) { body.set('cf_turnstile', t); return body; }
    if (typeof body === 'string') {
      var s = body.trim();
      if (s.charAt(0) === '{') { try { var o = JSON.parse(s); o.cf_turnstile = t; return JSON.stringify(o); } catch (e) { return body; } }
      return body + (body ? '&' : '') + 'cf_turnstile=' + encodeURIComponent(t);
    }
    if (body === undefined || body === null) { return 'cf_turnstile=' + encodeURIComponent(t); }
    return body;
  }

  // Seguir cual formulario esta usando la persona
  ['focusin', 'input', 'click', 'touchstart'].forEach(function (ev) {
    document.addEventListener(ev, function (e) { var f = e.target && e.target.closest ? e.target.closest('form') : null; if (f) { ultimoForm = f; } }, true);
  });

  // fetch
  if (window.fetch) {
    var fetchOriginal = window.fetch;
    window.fetch = function (recurso, opciones) {
      var url = (typeof recurso === 'string') ? recurso : (recurso && recurso.url) || '';
      var metodo = ((opciones && opciones.method) || (recurso && recurso.method) || 'GET').toUpperCase();
      if (metodo !== 'POST' || !esDestino(url)) { return fetchOriginal.apply(this, arguments); }
      var self = this, form = ultimoForm;
      return new Promise(function (resolver, rechazar) {
        esperarFicha(form, function (t) {
          var op = Object.assign({}, opciones || {});
          op.body = agregar(op.body, t);
          if (typeof op.body === 'string' && op.body.charAt(0) !== '{' && !(op.headers instanceof Headers)) {
            op.headers = Object.assign({}, op.headers || {});
            if (!op.headers['Content-Type'] && !op.headers['content-type']) { op.headers['Content-Type'] = 'application/x-www-form-urlencoded'; }
          }
          fetchOriginal.call(self, recurso, op).then(resolver, rechazar);
        });
      });
    };
  }

  // XMLHttpRequest (jQuery $.ajax, $.post)
  var abrirOriginal = XMLHttpRequest.prototype.open;
  var enviarOriginal = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function (metodo, url) {
    this.__gmDestino = String(metodo).toUpperCase() === 'POST' && esDestino(url);
    return abrirOriginal.apply(this, arguments);
  };
  XMLHttpRequest.prototype.send = function (body) {
    if (!this.__gmDestino) { return enviarOriginal.apply(this, arguments); }
    var xhr = this, form = ultimoForm;
    esperarFicha(form, function (t) { enviarOriginal.call(xhr, agregar(body, t)); });
  };

  // Envio normal de formularios (action="enviar.php"): solo si el sitio no lo maneja con JavaScript
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (e.defaultPrevented || !f || !f.getAttribute || !esDestino(f.getAttribute('action') || '')) { return; }
    var campo = f.querySelector('input[name="cf_turnstile"]');
    if (!campo) { campo = document.createElement('input'); campo.type = 'hidden'; campo.name = 'cf_turnstile'; f.appendChild(campo); }
    var t = tomarFicha(f);
    if (t) { campo.value = t; return; }
    e.preventDefault();
    esperarFicha(f, function (t2) { campo.value = t2; HTMLFormElement.prototype.submit.call(f); });
  }, false);

  // Una verificacion dentro de cada formulario con boton de envio
  window.gmTurnstileListo = function () {
    var forms = document.querySelectorAll('form');
    for (var i = 0; i < forms.length; i++) {
      var f = forms[i];
      if ((f.getAttribute('role') || '').toLowerCase() === 'search') { continue; }
      var boton = f.querySelector('button[type="submit"], input[type="submit"], button:not([type])');
      if (!boton) { continue; }
      var caja = document.createElement('div');
      caja.className = 'gm-turnstile';
      caja.style.cssText = 'margin:8px 0;';
      boton.parentNode.insertBefore(caja, boton);
      (function (form, caja) {
        var w = { form: form, caja: caja, id: null, ficha: '' };
        try {
          w.id = window.turnstile.render(caja, {
            sitekey: SITEKEY, appearance: 'interaction-only', language: 'es', 'refresh-expired': 'auto',
            callback: function (t) { w.ficha = t; },
            'expired-callback': function () { w.ficha = ''; },
            'error-callback': function () { w.ficha = ''; }
          });
          widgets.push(w);
        } catch (e) {}
      })(f, caja);
    }
  };
  var s = document.createElement('script');
  s.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=gmTurnstileListo';
  s.async = true; s.defer = true;
  (document.head || document.documentElement).appendChild(s);
})();