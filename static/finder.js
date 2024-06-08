let map;
let marker;

async function initMap() {

    const position = userLocation;
    const { Map } = await google.maps.importLibrary("maps");

    map = new Map(document.getElementById("map"), {
        zoom: 11,
        center: position,
    });

    const marker = new google.maps.Marker({
        map,
        position: position,
        icon: {                             
            url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
        }
      });

    placeMarker();
}

function placeMarker() {
    console.log("CONNECTED");

    for(let i = 0; i < markerList.length; i++){
        const currentMarker = (markerList[i]);
        const markerPosition = { lat: currentMarker[1], lng: currentMarker[2] };
        const name = currentMarker[0];
        const address = currentMarker[3];
    
        console.log("Placing marker at: ", markerPosition, " with name: ", name);
    
        const marker = new google.maps.Marker({
        map: map,
        position: markerPosition,
        title: name,
        });

        const infowindow = new google.maps.InfoWindow({
            content: name.concat("<br>", address), 
        })

        marker.addListener("click", () => {
            infowindow.open(map, marker);
        })

        marker.setMap(map);

        const eachItemBox = document.getElementById(`eachItemBox-${i + 1}`);

        eachItemBox.addEventListener("click", () => {
            infowindow.open(map, marker);
        });
    }

    console.log("Marker placed: ", marker);

}

initMap(); 

