/* --- script.js CORREGIDO --- */

// Funciones Globales
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function popupprivacy() {
    var popup = document.getElementById("popupprivacy");
    popup.classList.toggle("showpopuppolicies");
}

function popupwarranty() {
    var popup = document.getElementById("popupwarranty");
    popup.classList.toggle("showpopuppolicies");
}

function comparar() { 
    var popup = document.getElementById('comparePopup');
    if(popup) popup.classList.add('show-popup');
}

function closeCompare() {
    var popup = document.getElementById('comparePopup');
    if(popup) popup.classList.remove('show-popup');
}

// Cerrar popups al hacer click fuera
window.onclick = function(event) {
    var popup = document.getElementById('comparePopup');
    if (event.target == popup) closeCompare();
    
    var wppPopup = document.getElementById('whatsappPopup');
    if (event.target == wppPopup) wppPopup.classList.remove('show-popup');
}

// INICIO DEL DOM READY
$(document).ready(function() {

    // 1. CONFIGURACIÓN DE CARRUSELES ESTÁNDAR
    $('#owlc1').owlCarousel({ loop: true, margin: 10, autoplay: true, autoplayTimeout: 4000, responsiveClass: true, navText: ['', ''], navClass: ['owlprev', 'owlnext'], responsive: { 0: { items: 1, nav: false }, 600: { items: 2, nav: false }, 1000: { items: 3, nav: true, margin: 50 } } });
    $('#owlc2').owlCarousel({ loop: true, margin: 10, autoplay: true, autoplayTimeout: 4000, responsiveClass: true, navText: ['', ''], navClass: ['owlprev', 'owlnext'], responsive: { 0: { items: 1, nav: false }, 600: { items: 1, nav: false }, 1000: { items: 1, nav: false, loop: false, margin: 20 } } });
    $('#owlc3').owlCarousel({ loop: true, margin: 10, autoplay: true, autoplayTimeout: 7000, responsiveClass: true, navText: ['', ''], navClass: ['owlprev', 'owlnext'], responsive: { 0: { items: 2, nav: false }, 600: { items: 3, nav: false }, 1000: { items: 5, nav: false, loop: true, margin: 20 } } });
    
    $('#owlc5').owlCarousel({
        loop: true, margin: 20, nav: false, dots: false, autoplay: true, autoplayTimeout: 3000, autoplayHoverPause: true,
        responsive: { 0: { items: 2 }, 600: { items: 3 }, 1000: { items: 4 } }
    });

    // 2. CONFIGURACIÓN CARRUSEL DE VIDEOS (OWLC4)
    var videoCarousel = $('#owlc4');
    
    videoCarousel.owlCarousel({
        loop: true,
        margin: 20,
        nav: true, 
        dots: true,
        autoplay: false,
        // Configuración responsive explícita para mover de 1 en 1
        responsive:{
            0:{ 
                items: 1, 
                nav: true,
                slideBy: 1 // Mueve 1
            },
            600:{ 
                items: 2, 
                nav: true,
                slideBy: 1 // Mueve 1
            },
            1000:{ 
                items: 3, 
                nav: true,
                slideBy: 1 // Mueve 1 (IMPORTANTE)
            }
        },
        navText: ["<div class='nav-btn prev'>&#8249;</div>", "<div class='nav-btn next'>&#8250;</div>"]
    });

    // 3. LÓGICA DE VIDEOS VIMEO (CLICK-TO-PLAY)
    videoCarousel.on('click', '.testimonial-card', function(e) {
        // Si el clic fue en un botón de control, no hacemos nada (dejamos que el evento del botón actúe)
        if ($(e.target).closest('.ctrl-btn').length > 0) return;

        var cardWrapper = $(this);
        
        // Si ya está activo el video, no recargamos
        if (cardWrapper.hasClass('vimeo-active')) return;

        var vimeoId = cardWrapper.data('gm-video-id'); // 26-nov-2026: antes data-vimeo-id, que Vimeo auto-incrustaba al cargar
        var posterLayer = cardWrapper.find('.poster-layer');
        var placeholder = cardWrapper.find('.vimeo-placeholder')[0];
        var controlsBar = cardWrapper.find('.custom-player-controls');
        
        // Ocultar portada y mostrar controles
        posterLayer.fadeOut(300);
        cardWrapper.addClass('vimeo-active');
        controlsBar.removeClass('hidden'); 
        
        // Detener movimiento del carrusel por seguridad
        videoCarousel.trigger('stop.owl.autoplay');

        var options = {
            id: vimeoId,
            autoplay: true,
            muted: false,
            controls: false, // SIN CONTROLES NATIVOS (Barra oculta)
            loop: false,
            title: false,
            byline: false,
            portrait: false,
            autopause: false,
            dnt: true 
        };

        // Limpiar contenedor
        placeholder.innerHTML = "";
        var player = new Vimeo.Player(placeholder, options);
        
        // Referencias a botones
        var playPauseBtn = cardWrapper.find('.js-play-pause');
        var muteUnmuteBtn = cardWrapper.find('.js-mute-unmute');
        var fullscreenBtn = cardWrapper.find('.js-fullscreen');
        
        var iconPlay = playPauseBtn.find('.icon-play');
        var iconPause = playPauseBtn.find('.icon-pause');
        var iconSound = muteUnmuteBtn.find('.icon-sound');
        var iconMuted = muteUnmuteBtn.find('.icon-muted');

        // Eventos Player
        player.on('play', function() { 
            iconPlay.addClass('hidden'); 
            iconPause.removeClass('hidden'); 
        });

        player.on('pause', function() { 
            iconPlay.removeClass('hidden'); 
            iconPause.addClass('hidden'); 
        });

        player.on('ended', function() { 
            posterLayer.fadeIn(300); 
            cardWrapper.removeClass('vimeo-active');
            controlsBar.addClass('hidden');
            iconPlay.removeClass('hidden');
            iconPause.addClass('hidden');
            player.unload(); 
        });

        player.on('volumechange', function(data) {
            if (data.muted || data.volume === 0) {
                iconSound.addClass('hidden'); iconMuted.removeClass('hidden');
            } else {
                iconSound.removeClass('hidden'); iconMuted.addClass('hidden');
            }
        });

        // Click Botones
        playPauseBtn.off('click').on('click', function(e) {
            e.stopPropagation();
            player.getPaused().then(function(paused) {
                if (paused) { player.play(); } else { player.pause(); }
            });
        });

        muteUnmuteBtn.off('click').on('click', function(e) {
            e.stopPropagation();
            player.getMuted().then(function(muted) {
                player.setMuted(!muted);
            });
        });

        fullscreenBtn.off('click').on('click', function(e) {
            e.stopPropagation();
            player.requestFullscreen().catch(function(error) { console.log('Error FS:', error); });
        });
    });

    // 4. AÑO COPYRIGHT
    if(document.getElementById("year")) {
        document.getElementById("year").innerHTML = new Date().getFullYear();
    }

    // 5. VIDEO HERO (HEADER)
    var iframeHero = document.querySelector('#vimeo-player');
    // 26-nov-2026: el iframe se carga cuando entra en pantalla (ver index.html); el reproductor se arma ahí.
    window.gmInitHero = function() {
        if (!iframeHero || !iframeHero.getAttribute('src') || window.gmHeroReady) return;
        window.gmHeroReady = true;
        var playerHero = new Vimeo.Player(iframeHero);
        var btnPlayHero = document.getElementById('btn-video-play');
        var btnMuteHero = document.getElementById('btn-video-mute');
        
        var iconPauseHero = document.getElementById('icon-pause');
        var iconPlayHero = document.getElementById('icon-play');
        var iconMutedHero = document.getElementById('icon-muted');
        var iconSoundHero = document.getElementById('icon-sound');

        var isPlayingHero = true; 
        var isMutedHero = true;

        function updateHeroPlayIcon(playing) {
            if (playing) {
                iconPlayHero.classList.add('hidden-icon'); iconPauseHero.classList.remove('hidden-icon');
            } else {
                iconPlayHero.classList.remove('hidden-icon'); iconPauseHero.classList.add('hidden-icon');
            }
        }

        function updateHeroMuteIcon(muted) {
            if (muted) {
                iconSoundHero.classList.add('hidden-icon'); iconMutedHero.classList.remove('hidden-icon');
            } else {
                iconSoundHero.classList.remove('hidden-icon'); iconMutedHero.classList.add('hidden-icon');
            }
        }

        btnPlayHero.addEventListener('click', function() {
            if (isPlayingHero) { playerHero.pause(); isPlayingHero = false; } 
            else { playerHero.play(); isPlayingHero = true; }
            updateHeroPlayIcon(isPlayingHero);
        });

        btnMuteHero.addEventListener('click', function() {
            if (isMutedHero) { playerHero.setVolume(1); playerHero.setMuted(false); isMutedHero = false; } 
            else { playerHero.setVolume(0); playerHero.setMuted(true); isMutedHero = true; }
            updateHeroMuteIcon(isMutedHero);
        });

        playerHero.on('play', function() { isPlayingHero = true; updateHeroPlayIcon(true); });
        playerHero.on('pause', function() { isPlayingHero = false; updateHeroPlayIcon(false); });
    };
    if (iframeHero && iframeHero.getAttribute('src')) { window.gmInitHero(); }

    // 6. LÓGICA FORMULARIO WHATSAPP (POPUP)
    // 6. LÓGICA FORMULARIO WHATSAPP (CORREGIDO FINAL)
    var inputTelefono = document.querySelector("#telefono-popup-kommo10x");
    var iti;
    
    if (inputTelefono) {
        iti = window.intlTelInput(inputTelefono, { 
            initialCountry: "co", 
            separateDialCode: true,
            dropdownContainer: document.body,
            utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js", 
            placeholderNumberType: "MOBILE" 
        });

        // Evento para ajustar la posición si se hace scroll
        var handleChange = function() {
            var text = (iti.isValidNumber()) ? "Válido: " + iti.getNumber() : "Inválido";
        };
        
        inputTelefono.addEventListener('countrychange', function() { 
            inputTelefono.placeholder = iti.getNumberType() === 1 ? 'Ej: 300 1234567' : 'Número de Teléfono'; 
        });
    }

    let formWasSubmitted = false;
    var popupWpp = $('#whatsappPopup');
    var openBtn = $('#openPopupBtn');
    var closeBtn = $('.close-btn');
    var formPopup = $('#whatsappForm');
    var formView = $('#form-view');
    var thankYouView = $('#thank-you-view');

    openBtn.on('click', function() { 
        popupWpp.addClass('show-popup'); 
        if (typeof gtag === 'function') { gtag('event', 'clickchatwhatsapp_popup', { 'event_category': 'conversiones' }); }
        if (typeof fbq === 'function') { fbq('track', 'Lead'); }
    });

    function closePopup() {
        popupWpp.removeClass('show-popup');
        if (!formWasSubmitted) {
            setTimeout(function() {
                formView.show(); thankYouView.hide(); 
                if(formPopup.length) formPopup[0].reset();
                $('#submitBtn').prop('disabled', false).text('Enviar y Chatear en WhatsApp');
            }, 500);
        }
    }
    
    closeBtn.on('click', closePopup);
    popupWpp.on('click', function(event) { if ($(event.target).is(popupWpp)) { closePopup(); } });

    formPopup.on('submit', function(event) {
        event.preventDefault();
        var nombreVal = $('#nombre').val().trim();
        var correoVal = $('#correo').val().trim();
        var asesoresVal = $('#asesores').val();
        var fullPhone = iti.getNumber(); 
        var isPhoneValid = fullPhone && fullPhone.length >= 8; 

        if (nombreVal === "" || correoVal === "" || asesoresVal === null || asesoresVal === "" || !isPhoneValid) {
            if (!isPhoneValid) { alert('Por favor, escribe un número de teléfono completo.'); } 
            else if (asesoresVal === null || asesoresVal === "") { alert('Por favor, selecciona el número de asesores.'); } 
            else { alert('Por favor, completa todos los campos.'); }
            return;
        }

        // 26-nov-2026: Turnstile se carga al abrir el formulario; si el token aún no está, esperar hasta 10 s.
        if (window.gmLoadTurnstile) { window.gmLoadTurnstile(); }
        var tsTok = (document.querySelector('#whatsappForm [name="cf-turnstile-response"]') || {}).value || '';
        if (!tsTok && (window.gmTsWait = (window.gmTsWait || 0) + 1) <= 20) {
            $('#submitBtn').prop('disabled', true).text('Verificando...');
            setTimeout(function() { $('#submitBtn').prop('disabled', false); formPopup.trigger('submit'); }, 500);
            return;
        }
        window.gmTsWait = 0;

        var submitButton = $('#submitBtn');
        submitButton.prop('disabled', true).text('Enviando...');
        
        // Obtenemos los UTMs directamente de la URL (usando la función que ya tienes arriba en script.js)
        var formData = { 
            nombre: nombreVal, 
            correo: correoVal, 
            telefono: fullPhone, 
            asesores: asesoresVal,
            utm_source: getParameterByName('utm_source'), 
            utm_medium: getParameterByName('utm_medium'),
            utm_campaign: getParameterByName('utm_campaign'), 
            utm_term: getParameterByName('utm_term'),
            utm_content: getParameterByName('utm_content'),
            gclid: getParameterByName('gclid'),
            fbclid: getParameterByName('fbclid'),
            cf_turnstile: (document.querySelector('#whatsappForm [name="cf-turnstile-response"]') || {}).value || ''
        };

        var whatsappMessage = "Hola mi nombre es " + formData.nombre + ", me interesa contratar sus servicios, adjunto mis datos: Mi número telefonico es " + formData.telefono + ", mi correo es " + formData.correo + " y cuento con un equipo " + formData.asesores + ".";
        var newWhatsappUrl = 'https://api.whatsapp.com/send?phone=573169062242&text=' + encodeURIComponent(whatsappMessage); 
        $('#whatsapp-redirect-link').attr('href', newWhatsappUrl);

        $.ajax({
            type: 'POST', 
            url: 'enviar.php', 
            data: formData, 
            dataType: 'json',
            success: function(response) {
                $("#loading").hide(); 
                if (response && response.status === 'success') {
                    
                    // Evento para Google Tag Manager
                    window.dataLayer = window.dataLayer || []; 
                    window.dataLayer.push({'event': 'FormWhatsapp'});
                    
                    formWasSubmitted = true;
                    if (typeof gtag === 'function') { gtag('event', 'form_submit_whatsapp_kommo10x', { 'event_category': 'conversiones' }); }
                    if (typeof fbq === 'function') { fbq('track', 'Lead'); }
                    
                    formView.hide(); 
                    thankYouView.show();
                } else {
                    alert('Hubo un error al enviar tu mensaje. Por favor, intenta de nuevo.');
                    if (window.turnstile) { try { window.turnstile.reset(); } catch (e) {} }
                    submitButton.prop('disabled', false).text('ENVIAR Y CHATEAR EN WHATSAPP');
                }
            },
            error: function() {
                $("#loading").hide();
                // En caso de error de conexión, se mantiene el fallback de abrir WP directo que tenías
                window.open(newWhatsappUrl, '_blank');
                formView.hide(); 
                thankYouView.show();
            }
        });
    });

    // Otros eventos
    $(".clickllamar").click(function () {
        if (typeof gtag === 'function') gtag('event', 'clickllamar', { 'event_category': 'conversiones' });
        if (typeof fbq === 'function') fbq('track', 'Lead');
    });
    $(".clickcompartir").click(function () {
        if (typeof gtag === 'function') gtag('event', 'clickcompartir', { 'event_category': 'conversiones' });
    });

    var acc = document.getElementsByClassName("accordion");
    for (let i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) { panel.style.maxHeight = null; } else { panel.style.maxHeight = panel.scrollHeight + "px"; }
        });
    }
});