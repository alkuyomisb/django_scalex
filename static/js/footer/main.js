$(document).ready(function () {
  // jQuery plugin example:
  $("#particles").particleground({
    dotColor: "#ffffff",
    lineColor: "#ffffff",
    particleRadius: 12, // Dot size
    lineWidth: 0.5,
    proximity: 80,
    // How close two dots need to be before they join
    parallax: true,
    parallaxMultiplier: 3,
    // The lower the number, the more extreme the parallax effect
    onInit: function () {},
    onDestroy: function () {},
  });
  // Fixed navbar
  $(window).scroll(function () {
    var sticky = $(".navbar-main"),
      scroll = $(window).scrollTop();

    if (scroll >= 100) sticky.addClass("navbar-fixed");
    else sticky.removeClass("navbar-fixed");
  });

  // ===== Scroll to Top ====
  $(window).scroll(function () {
    if ($(this).scrollTop() >= 50) {
      // If page is scrolled more than 50px
      $("#return-top").fadeIn(200); // Fade in the arrow
    } else {
      $("#return-top").fadeOut(200); // Else fade out the arrow
    }
  });

  // Return to top
  $("#return-top").click(function () {
    // When arrow is clicked
    $("body,html").animate(
      {
        scrollTop: 0, // Scroll to top of body
      },
      500
    );
  });

  $("#carousel-spotlight").owlCarousel({
    loop: true,
    nav: true,
    dots: true,
    navText: "",
    lazyLoad: true,
    autoplay: false,
    autoplayTimeout: 2000,
    rtl: true,
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
        margin: 15,
      },
      1200: {
        items: 3,
        margin: 35,
      },
    },
  });

  $("#carousel-registrars").owlCarousel({
    loop: true,
    nav: true,
    dots: false,
    navText: "",
    lazyLoad: true,
    autoplay: false,
    autoplayTimeout: 2000,
    margin: 10,
    rtl: true,
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
      },
      1200: {
        items: 3,
      },
    },
  });

  $("#carousel-lt-event").owlCarousel({
    loop: true,
    nav: true,
    dots: false,
    navText: "",
    lazyLoad: true,
    autoplay: false,
    autoplayTimeout: 2000,
    margin: 10,
    rtl: true,
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
        margin: 10,
      },
      1280: {
        items: 2,
        margin: 25,
      },
    },
  });

  //--------------------- end of document ready
});

$("#carouselBanner").carousel({
  pause: "false",
});

// Tooltip
$('[data-toggle="tooltip"]').tooltip();
$('[data-toggle="popover"]').popover();

// Loader
$(window).on("load", function () {
  $(".loader-overlay").delay(2000).fadeOut("slow");
});

AOS.init();
