  function initMap(lt, lg) {
                    /*
                    Google Map Function
                    This function queries Google Map API.
                    Return: Map
                     */

                  // The location of place
                  var place = { lat: lt, lng: lg};
                  if (lt == null && lg == null) {
                        place = { lat: 0, lng: 0 };
                  }
                  // The map, centered at the place
                  const map = new google.maps.Map(document.getElementById("map"), {
                    zoom: 6,
                    center: place,
                  });
                  // The marker, positioned at the place
                  const marker = new google.maps.Marker({
                    position: place,
                    map: map,
                  });
                }