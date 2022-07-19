var calculate_dmg
var unlock
var update_hp
var get_hp
var get_img 
var get_pm_id
var get_speed
var get_move_id
var get_atk
var get_def
var get_move_dmg 
var get_type_rate
var get_pm_type1
var get_pm_type2
var get_move_type
var get_alive
var show_move
var show_pm
var hide_move
var hide_pm

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


   calculate_dmg = function(atk_pm, def_pm,move_id){
      dmg = get_atk(atk_pm)+get_dmg(move_id)-get_def(def_pm)
      dmg = dmg * get_type_rate(get_move_type,get_pm_type1(atk_pm),get_pm_type2(def_pm))
      return dmg
   }

   update_hp = function(user_id, pm_id,chp){
//      correct_pm_hp = chp
//      user_id_alive -=1
   }
   get_hp = function(user_id, pm_id){
      return pm_hp //from correct DB
   }
   get_move_img = function(move_id,user_id){
      
   }
   get_pm_img = function(pm_id,user_id){
      if(user_id = user){
         //try
            //clean user img
         //load user img
      }else{
         //try
            //clean npc img
         //load npc img
      }
   }
   get_pm_num = function(){
      return pm_num //from button
   }
   get_speed = function(pm_num,user_id){
      return pm_speed
   }
   get_move_id = function(num, user){
      return move_id //from movelist
   }
   get_atk = function(pm_id){
      return atk
   }
   get_def = function(pm_id){
      return def
   }
   get_move_dmg = function(move_id){
      return dmg
   }
   get_type_rate  = function(move_type,type1,type2){
      return rate //from type DB
   }
   get_pm_type1 = function(pm_id){
      return pm_type1
   }
   get_pm_id = function(num, user_id){
      return pm_id
   }
   get_pm_type2 = function(pm_id){
      //try
      //   return pm_type2
      //   return null
   }
   get_alive = function(user_id){
      return alive
   }
   show_move = function(){

   }
   show_pm = function(){
//      for(user_pm_list){
  //       if(get_hp(pm_id_i) > 0){
    //        show
      //   }
      //}
   }
   hide_pm = function(){
//hide all
   }
   hide_move = function(){
//      hide all
   }
   get_pm_img(1,user)
   get_pm_img(1,npc)
});



function move_onclick(num){
   hide_pm()
   hide_move()
   var action_lock_user = true
   var action_lock_npc = true
   var chp = get_hp(user,pm)
   var cnhp = get_hp(npc,pm)
   var umid = get_move_id(num,user)
   var nmid = get_move_id(random(),npc)
   var pm1_id = get_pm_id(1,user)
   var npm1_id = get_pm_id(1,npc)
   
   if(get_speed(1,user) >= get_speed(1,npc)){
         action_lock_user = false
         cnhp -= calculate_dmg(pm1_id, npm1_id, umid)
         if(cnhp <=0){
            action_lock_npc = false
            cnhp = 0
         }
   }
   if(action_lock_npc === true){
      action_lock_npc = false
      chp -= calculate_dmg(npm1_id,pm1_id,nmid)
      if(chp <=0){
         action_lock_user = false
         chp = 0
      }
   }
   if(action_lock_user === true){
      action_lock_user = false
      cnhp -= calculate_dmg(pm1_id, npm1_id, umid)
      if(cnhp <=0){
         cnhp = 0
      }
   }
   update_hp(user,pm1_id,chp)
   update_hp(npc,npm1_id,cnhp)
   if(chp === 0){
      if(get_alive(user) === 0){
         return lose
      }
      show_pm()
   }
   if(cnhp === 0){
      if(get_alive(npc) === 0){
         return win
      }
      change_pm(get_alive(npc),npc)
   }
   show_pm()
   show_move()
}



function change_onclick(num){
   pm1_id = get_pm_id(num)
   hp = get_hp(pm1_id)
   change_pm(num,user)
   if(get_hp(pm1_id) !== 0){
      hp = get_hp(pm1_id)
      hp -= calculate_dmg(pm1_id,npm1_id,umid)
      update_hp(pm1_id,hp)
   }
}



//is the pm_id will save in the tools?
function change_pm(num,user_id){
   if(user){
      get_pm_img(num,user) 
      user_tools_id = get_pm_id(num,user_id)
   }
   else{
      get_pm_img(num,npc)
      npc_tools_id = get_pm_id(num,user_id)
   }
}
