$('#sideNavToggle').on('click', function () {
    if ($("#mySidenav").width() == 0) {
        $("#mySidenav").width(250);
        $('#main').css({"margin-left": "250px"})
    } else {
        $("#mySidenav").width(0)
        $('#main').css({"margin-left": "0px"})
    }
});

