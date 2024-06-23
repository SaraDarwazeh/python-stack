
var count =1;
var countElement = document.getElementById("#likes-count");

function likes()

{   console.log(count);
    count++;
    countElement.innerHTML="<h3><span>count</span> Like(s)</h3>;"
}