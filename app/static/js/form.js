document.getElementById("connexion").addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById("user_input");
    const result = document.getElementById('result');
    const message = document.getElementById('message');
    const end_message = document.getElementById('end');
    const address = document.getElementById('address');
    const maps = document.getElementById('map');
    const footer = document.getElementById('foot');
    const data = new FormData(this);

    const xhr = new XMLHttpRequest();
    let erreur;


        xhr.onreadystatechange = function(event) {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.response);
                var lt = this.response['lat'];
                var lg = this.response['lng'];

                maps.classList.add('display');
                footer.style.position = "initial";
                result.innerHTML = this.response['wiki'];
                address.innerHTML = this.response['address'];
                end_message.innerHTML = this.response['end_mess'];

                message.innerHTML = this.response['message'];

                if (lt == null) {
                    maps.innerHTML = null;
                } else {
                    initMap(lt, lg);
                }

            } else {
                console.log(this.readyState, this.status, this.response);

            }

        }

        xhr.open("POST", "/process", true);
        xhr.responseType = "json";
        xhr.send(data);

        return false;



});


