const IMG_OFFSET = 100;
const IMG_HEIGHT = 150;
const CANVAS_WIDTH = 720;
const CANVAS_TRUE_HEIGHT= 500;
const CANVAS_HEIGHT = 300;
const IMG_SCALE = 192
const PLAYER_ORI_POS = -2 * IMG_OFFSET;

var poke_json;
var poke_json_ene;
var poke_choice;


var poke_health = 100;

var buttonArr = [[100,415],[100+200+50,415],[100+200+50,415+35+10],[100,415+35+10]]
var buttonText = ["Redu. HP","Animate","See Team","Game Condition"]

var animation_f;
var player_X = PLAYER_ORI_POS;
var con_mov;

var poke_actor_img = new Image();
var poke_trainer_img = new Image();

var finish_round;
var show_team;

var poke_move = [];
var ene_move = [];
var poke_actors = [];
var ene_actors = [];

var background_img = new Image();

$(document).ready(function (){
   ini_game();
   game_start();

});



function ini_game(){
   poke_actors = [];
   ene_actors = [];
   poke_choice = 0;
   for (var i = 0; i < 6; i++){
      let ran_poke = Math.floor((Math.random() * 151) + 1);
      console.log(ran_poke)
      $.ajax({
         url: '../PHP/get_methods_poke.php',
         data: {"get_all_data": ran_poke},
         async: false,
         success(e){
            poke_actors.push(JSON.parse(e));
         }
      });
   }
   poke_json = poke_actors[poke_choice];
   //Getting pokemon for ene
   for (var i = 0 ; i < 6 ; i++){
      let ran_poke = Math.floor((Math.random() * 151) + 1);
      console.log(ran_poke)
      $.ajax({
         url: '../PHP/get_methods_poke.php',
         data: {"get_all_data": ran_poke},
         async: false,
         success(e){
            ene_actors.push(JSON.parse(e));
         }
      });

   }
   poke_json_ene = ene_actors[0];

}

function game_start(){
   var c = document.getElementById("battle_game")
   var ctx = c.getContext('2d')
   ctx.imageSmoothingEnabled = false; // make it not blurry
   finish_round = false;
   show_team = false;
   //Getting pokemon for player


   background_arr = ['island.png','mountain.png','plains.png'];
   let ran_bg = Math.floor((Math.random() * 3));

   background_img.src = '../img/'+background_arr[ran_bg];
   background_img.onload = function () {
      console.log(background_img)
      ctx.drawImage(background_img, 0, -90)
      load_player(ctx);
      load_trainer(ctx);
      load_UI(ctx)
   }

   c.addEventListener('click', function (e){
      if (!finish_round && !show_team){
         var button_choice = button_handler(c, ctx, e)
         if (button_choice === 0){
            poke_health-=10;
            dmg_take = 10;
            requestAnimationFrame(reduce_hp_anim)
         }
         else if (button_choice=== 1){
            animation_f = 30;
            con_mov = true;
            requestAnimationFrame(animate_user)
         }

         else if (button_choice === 2){
            create_win(ctx);
            finish_round = true;

         }
         else if (button_choice === 3){
            show_team = true;
            load_team(ctx);


         }
      }
      else{
         const canvas = c.getBoundingClientRect();
         var mouseX = ((e.clientX - canvas.left) / (canvas.right - canvas.left)) * c.width;
         var mouseY = ((e.clientY - canvas.top) / (canvas.bottom  - canvas.top)) * c.height;
         if (finish_round){
            if (mouseX > 310 && mouseX < 510 && mouseY>300&& mouseY < 330){
               ini_game();
               game_start();
            }
         }
         else if (show_team){
            var team_choice = button_team(ctx, c, e);
            if (team_choice === poke_choice){
               console.log("Same")
            }
            else if(team_choice === -1){
               console.log("No choice")
            }
            else {
               poke_json = poke_actors[team_choice];
               console.log(poke_json);
               ctx.drawImage(background_img, 0, -90)
               load_trainer(ctx);
               load_player(ctx);
               load_UI(ctx)
               poke_choice= team_choice;
               show_team = false;
            }
            if (mouseX > 470 && mouseX < 670 && mouseY > 425 && mouseY < 460){
               load_UI(ctx)
               show_team = false;
            }
         }

      }


   })
   // Animation functions
   function reduce_hp_anim(){
      if (dmg_take>0 && poke_health>=0){
         poke_health--;
         hp_UI(ctx)
         requestAnimationFrame(reduce_hp_anim)

      }
      dmg_take--;
   }

   function animate_user(){
      if (animation_f>0){
         ctx.drawImage(background_img, 0, -90)
         if (con_mov){
            player_X -=30;
         }
         if (player_X < -420){
            con_mov = false;
         }
         animate_user_load(ctx);
         animate_trainer_load(ctx);
         load_UI(ctx)
         console.log("sad")
         requestAnimationFrame(animate_user)

      }
      else {
         ctx.drawImage(background_img, 0, -90)
         player_X = PLAYER_ORI_POS;
         animate_user_load(ctx);
         animate_trainer_load(ctx);
         load_UI(ctx)
         console.log("sad")

      }
      animation_f--;
   }
}


function create_win(ctx){
   ctx.fillStyle = "#ffbaae";
   ctx.fillRect(0,0, CANVAS_WIDTH, CANVAS_TRUE_HEIGHT);
   ctx.font = '20px Arial';
   ctx.fillStyle = '#6e6c6c'
   ctx.fillText("WIN", CANVAS_WIDTH/2, CANVAS_TRUE_HEIGHT/2);

   buttons_UI(ctx, (CANVAS_WIDTH/2)-50,(CANVAS_TRUE_HEIGHT/2)+50, "Next Trainer");

}

function animate_user_load(ctx){
   ctx.translate(IMG_OFFSET, IMG_HEIGHT);
   ctx.scale(-1, 1);
   ctx.drawImage(poke_actor_img, player_X, IMG_HEIGHT - CANVAS_HEIGHT / 2, IMG_SCALE, IMG_SCALE)
   ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function animate_trainer_load(ctx){
   ctx.drawImage(poke_trainer_img, CANVAS_WIDTH-IMG_OFFSET-IMG_SCALE,IMG_HEIGHT, IMG_SCALE,IMG_SCALE)

}

function button_handler(c, ctx, e){
   const canvas = c.getBoundingClientRect();
   var mouseX = ((e.clientX - canvas.left) / (canvas.right - canvas.left)) * c.width;
   var mouseY = ((e.clientY - canvas.top) / (canvas.bottom  - canvas.top)) * c.height;
   console.log(mouseX, mouseY);

   if(mouseX > 100 && mouseX < 300 && mouseY > 415 && mouseY<450){
      console.log("1")
      return 0;
   }
   else if (mouseX > 350 && mouseX < 550 && mouseY > 415 && mouseY<450){
      console.log("2")
      return 1;
   }
   else if(mouseX > 100 && mouseX < 300 && mouseY > 460 && mouseY<500){
      console.log("3")
      return 2;
   }
   else if (mouseX > 350 && mouseX < 550 && mouseY > 460 && mouseY<500){
      console.log("4")
      return 3;
   }


   return -1;

}

function load_team(ctx){
   ctx.fillStyle = "#ffbaae";
   ctx.fillRect(0,400,CANVAS_WIDTH, 100)
   ctx.fillStyle = '#F5F5F5FF';
   var posX = 10;
   var imgX = -5;
   for (var i = 0; i < 6; i++){
      let poke_img_loop = new Image();
      ctx.fillRect(posX,425,50, 50);
      posX += 60;
      poke_img_loop.src=poke_actors[i]['img_link'];
      poke_img_loop.onload = function () {
         ctx.drawImage(poke_img_loop, imgX, 400);
         imgX+=60;
      }
      console.log(poke_img_loop)
   }
   buttons_UI(ctx, CANVAS_WIDTH-250,425, "Back")
}

function button_team(ctx, c, e){
   const canvas = c.getBoundingClientRect();
   var mouseX = ((e.clientX - canvas.left) / (canvas.right - canvas.left)) * c.width;
   var mouseY = ((e.clientY - canvas.top) / (canvas.bottom  - canvas.top)) * c.height;
   console.log(mouseX, mouseY);
   var posX = 10;
   for (var i = 0 ; i < 6; i++){
      if(mouseX > posX && mouseX < posX+50 && mouseY > 425 && mouseY<475){
         console.log("1")
         return i;
      }
      posX+=60;
   }



   return -1;
}

function load_UI(ctx){

   ctx.fillStyle = "#ffbaae";
   ctx.fillRect(0,400,CANVAS_WIDTH, 100)

   ctx.fillStyle = '#F5F5F5FF';
   ctx.fillRect(0,0, (1/3)*CANVAS_WIDTH, 50);

   ctx.fillStyle = '#F5F5F5FF';
   ctx.fillRect(CANVAS_WIDTH-(1/3)*CANVAS_WIDTH,0, (1/3)*CANVAS_WIDTH, 50);

   hp_UI(ctx);
   hp_UI_ene(ctx);
   for (var i = 0 ; i < 4; i++){
      buttons_UI(ctx, buttonArr[i][0],buttonArr[i][1], buttonText[i]);
      buttons_UI(ctx, buttonArr[i][0],buttonArr[i][1], buttonText[i]);
      buttons_UI(ctx, buttonArr[i][0],buttonArr[i][1], buttonText[i]);
      buttons_UI(ctx, buttonArr[i][0],buttonArr[i][1], buttonText[i]);
   }
   text_UI(ctx, 10, 20, poke_json['display_name'])


   //hp_UI_ene(ctx);

}

function buttons_UI(ctx, posX, posY, text){
   ctx.fillStyle = "#382c2e";
   butH = 35;
   butW = 200;

   ctx.fillRect(posX,posY,butW, butH)

   ctx.font = '20px Arial';
   ctx.fillStyle = '#e5dddd'
   ctx.fillText(text, posX+50, posY+25);
}


function hp_UI_ene(ctx){
   ctx.fillStyle = "#96d152";
   var health_width = ((1/3)*CANVAS_WIDTH)*(4/5)
   ctx.fillRect(CANVAS_WIDTH-health_width-40,25, health_width, 10);
   text_UI(ctx, CANVAS_WIDTH-health_width-40, 20, poke_json_ene['display_name'])
}


function text_UI(ctx, posX, posY, display_name){
   ctx.font = '20px Arial';
   ctx.fillStyle = '#4b4646'
   console.log(display_name)
   ctx.fillText(display_name, posX, posY);
}

function hp_UI(ctx){
   ctx.fillStyle = "#ffffff";
   var health_width = ((1/3)*CANVAS_WIDTH)*(4/5)
   ctx.fillRect(10,25, health_width, 10);
   ctx.fillStyle = "#96d152";
   ctx.fillRect(10,25, health_width*(poke_health/100), 10);

}

function load_player(ctx) {

   poke_actor_img.src = poke_json['img_link'];
   poke_actor_img.onload = function () {
      ctx.translate(IMG_OFFSET, IMG_HEIGHT);
      ctx.scale(-1, 1);
      ctx.drawImage(poke_actor_img, player_X, IMG_HEIGHT - CANVAS_HEIGHT / 2, IMG_SCALE, IMG_SCALE)
      ctx.setTransform(1, 0, 0, 1, 0, 0);

   }
}




function load_trainer(ctx){
   poke_trainer_img.src = poke_json_ene['img_link'];
   poke_trainer_img.onload = function (){
      ctx.drawImage(poke_trainer_img, CANVAS_WIDTH-IMG_OFFSET-IMG_SCALE,IMG_HEIGHT, IMG_SCALE,IMG_SCALE)
      console.log(poke_trainer_img)
   }
}

