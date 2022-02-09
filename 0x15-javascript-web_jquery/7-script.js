// JavaScript script that fetches the character name

$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
});
