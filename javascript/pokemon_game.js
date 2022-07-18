$(document).ready(function (){


   var poke_actor_img = new Image();

   $.ajax({
      url: '../PHP/get_methods_poke.php',
      data: {"get_img": "nidoran-f"},
      async: false,
      success(e){
         console.log(e)
         poke_actor_img.src = e;
      }
   })


   var c = document.getElementById("battle_game")
   var ctx = c.getContext('2d')
   ctx.imageSmoothingEnabled = false; // make is not blurry
   ctx.drawImage(poke_actor_img, 50,50, 192,192)

});

