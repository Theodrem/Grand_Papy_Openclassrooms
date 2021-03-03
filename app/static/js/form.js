/*
  Listen to the click event on the submit element
*/
document.getElementById("connexion").addEventListener('submit', function(e) {

    e.preventDefault();

    /*All the constants that represent an Html element*/

    const name = document.getElementById("user_input");
    const result = document.getElementById('result');
    const message = document.getElementById('message');
    const end_message = document.getElementById('end');
    const address = document.getElementById('address');
    const maps = document.getElementById('map');
    const footer = document.getElementById('foot');

    const data = new FormData(this); //Constant contain data

    const xhr = new XMLHttpRequest(); //Constant represent xhr request
    let erreur;


        xhr.onreadystatechange = function(event) {
        /* Launch the ajax request*/
            result.innerHTML = "<img src='static/image/loader.gif' id='loader'>" //Display gif launcher
            if (this.readyState == 4 && this.status == 200) {
            /*If request is ok*/
                console.log(this.response);
                var lt = this.response['lat']; //get latitude
                var lg = this.response['lng']; //get longitude

                maps.classList.add('display');
                footer.style.position = "initial"; //Change position of the footer
                result.innerHTML = this.response['wiki']; //Display wiki message
                address.innerHTML = this.response['address']; //Display address
                end_message.innerHTML = this.response['end_mess']; // Display end message

                message.innerHTML = this.response['message']; // Display message

                if (lt == null) {
                    maps.innerHTML = null;
                } else {
                    initMap(lt, lg); // Display map
                }

            } else {
                console.log(this.readyState, this.status, this.response);

            }

        }


        xhr.open("POST", "/process", true);
        xhr.responseType = "json"; // Data in json format
        xhr.send(data);

        return false;



});


