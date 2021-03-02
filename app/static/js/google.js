  function initMap(lt, lg) {
                  // The location of Uluru
                  var place = { lat: lt, lng: lg};
                  if (lt == null && lg == null) {
                        place = { lat: 0, lng: 0 };
                  }
                  // The map, centered at Uluru
                  const map = new google.maps.Map(document.getElementById("map"), {
                    zoom: 6,
                    center: place,
                  });
                  // The marker, positioned at Uluru
                  const marker = new google.maps.Marker({
                    position: place,
                    map: map,
                  });
                }