var modal = document.getElementById('myModal');

var images = document.getElementsByClassName('imgs');
var descriptions = document.getElementsByClassName('image-descrips');

for(i=0; i<images.length; i++){
var modalImage = document.getElementById('img1');
var captionText = document.getElementById('caption');
var modalDescription = document.getElementById('description');


images.item(i).onclick = function(){
modal.style.display = 'block';
modalImage.src = this.src;
captionText.innerHTML = this.alt;

};
}

var span = document.getElementsByClassName("close")[0];


span.onclick = function(){
modal.style.display = "none";
};

console.log('gdcdgdhhdhhd')