/**
 * Created by lechkaiel on 12/22/16.
 */


/*
for(var i = 0; i < 5; i++) {
    var myFavoriteFoods = ["hummus", "spaghetti", "rice bowl", "peanut butter", "chowder"];
    var favoriteFood = prompt("What is one of your favorite foods?");
    var listItem = document.createElement("li");
    listItem.innerHTML = favoriteFood;
    if(myFavoriteFoods.includes(favoriteFood)){
        listItem.style.color = "green";
    }else{
        listItem.style.color = "red";
    }
    document.getElementById("foodList").appendChild(listItem);
} */

// dice game

function diceEmUp() {
    var n = document.getElementById("diceCount").value;
    var sumIt = 0;
    for(var i = 0; i < n; i++) {
        var randomNumber = Math.floor(Math.random() * 6) + 1;
        sumIt += randomNumber;
        console.log(randomNumber);
        var diceImage = document.createElement("img");
        var imageArray = ["images/dice_one.jpg","images/dice_two.png","images/dice_three.png","images/dice_four.png","images/dice_five.png","images/dice_six.png"];
        diceImage.setAttribute("src",imageArray[randomNumber - 1]);
        document.getElementById("diceHolder").appendChild(diceImage);
        allowClick("stopIt");
    }
    var sumStatement = document.createElement("p");
    sumStatement.innerHTML = "You rolled the dice " + n + " times and the sum is " + sumIt;
    document.getElementById("divInput").appendChild(sumStatement);
}

function allowClick(id) {
  if(id == "stopIt"){
     document.getElementById('stopIt').onclick = null;
     }
}