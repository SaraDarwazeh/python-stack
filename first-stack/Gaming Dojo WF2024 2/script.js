var imgArr = ["img/stonepunk.png", "img/pixel-ninjas-2.png ", "img/cafe-neko.png "];
var index = 0;
var count = 0;

function slidRight(element) {
    var img = document.getElementById('main-img');
    console.log(element);
    index++;
    if (index <= 2) {
        img.src = imgArr[index];
        document.getElementById(index).classList.add("selected");
        document.getElementById(index - 1).classList.remove("selected");
    }
    else {
        index = 0;
        document.getElementById(index).classList.add("selected");
        document.getElementById(2).classList.remove("selected");
        img.src = imgArr[index];
    }
}



function slidLeft(element) {
    var img = document.getElementById('main-img');
    index--;

    if (index >= 0) { img.src = imgArr[index]; document.getElementById(index).style.background = ('#9901FF'); }
    else { index = 2; img.src = imgArr[index]; document.getElementById(index).style.background = ('#9901FF'); }

}
function addTocart(element) {
    count++;
    var txt = document.getElementById('cart-items');
    txt.innerText = count;
}
function alertLinux() {
    alert("This game is supported on Linux");
}
