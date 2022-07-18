const IMG_OFFSET = 100;
const IMG_HEIGHT = 150;
const CANVAS_WIDTH = 720;
const CANVAS_HEIGHT = 300;
const IMG_SCALE = 192


$(document).ready(function (){
   var c = document.getElementById("battle_game")
   var ctx = c.getContext('2d')
   ctx.imageSmoothingEnabled = false; // make it not blurry

   background_arr = ['island.png','mountain.png','plains.png'];
   var background_img = new Image();
   background_img.src = '../img/island.png';
   background_img.onload = function () {
      console.log(background_img)
      ctx.drawImage(background_img, 0, -90)
      load_player(ctx);
      load_trainer(ctx);
      load_UI(ctx)
   }



});

function load_UI(ctx){
}

function load_player(ctx){
   /*
   var poke_arr = [];
   for (var i = 0; i < 6;i++){
      let x = Math.floor((Math.random()*151)+1);
      poke_arr.push(x);
   }

   console.log(poke_arr);*/

   $.ajax({
      url: '../PHP/get_methods_poke.php',
      data: {"get_img": "nidoran-f"},
      async: false,
      success(e){
         console.log(e)
         var poke_actor_img = new Image();
         poke_actor_img.src = e;
         poke_actor_img.onload = function (){
            console.log(poke_actor_img)
            ctx.translate(IMG_OFFSET,IMG_HEIGHT);
            ctx.scale(-1,1);
            ctx.drawImage(poke_actor_img,-2*IMG_OFFSET,IMG_HEIGHT-CANVAS_HEIGHT/2, IMG_SCALE,IMG_SCALE)
            console.log(poke_actor_img)
            ctx.setTransform(1,0,0,1,0,0);

         }
      }
   });
}




function load_trainer(ctx){
   $.ajax({
      url: '../PHP/get_methods_poke.php',
      data: {"get_img": "bulbasaur"},
      async: false,
      success(e){
         console.log(e)
         var poke_actor_img = new Image();
         poke_actor_img.src = e;
         poke_actor_img.onload = function (){
            ctx.drawImage(poke_actor_img, CANVAS_WIDTH-IMG_OFFSET-IMG_SCALE,IMG_HEIGHT, IMG_SCALE,IMG_SCALE)
            console.log(poke_actor_img)
         }
      }
   });
}


