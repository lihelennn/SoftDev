//window.requestAnimationFrame(<fxn>)

/*
Helen Li
SoftDev2 pd 3
HW 2b -- Dot, Dot, Dot
2016-02-22
*/

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var s = document.getElementById("stop");
var circ=document.getElementById("circle");

var width = c.width;
var height = c.height;

var radius = 0;
var expanding = true;

//Draw the outer rectangle 
function drawOutside(){
    ctx.rect(0,0,width,height);
    ctx.stroke();
}

drawOutside();

//Event listener for drawing on the canvas
//c.addEventListener("click",draw);
s.addEventListener("click",stop);
circ.addEventListener("click",animate);

function drawDot(r){
    ctx.arc(width/2,height/2,r,0,Math.PI*2);
    ctx.stroke();
    ctx.fill();
}

function animate(e){
    if (expanding){
	radius++;
    }else{
	radius--;
    }
    if (radius == width/2){
	expanding = false;
    }else{
	if (radius == 0){
	    expanding = true;
	    }
    }
    drawDot(radius);

}
    


/*
//Clear the canvas
function clear(e){
    e.preventDefault();
    clickNum=0;
    ctx.clearRect(0,0,width,height);
    drawOutside();
}
*/
