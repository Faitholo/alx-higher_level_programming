// JavaScript script that updates the text color of the <header> element to red (#FF0000) 
// when the user clicks on the tag DIV#red_header

$('DIV#red_header').click(function () {
    $('header').css({ color: '#FF0000' });
});
