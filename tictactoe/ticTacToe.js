/**
 * Created by lechkaiel on 12/27/16.
 */


var arrayXO = ["*","*","*","*","*","*","*","*","*"];

var turn = 0;


function updateArray(divid, turnString){
    for (var i = 1; i < 10; i++){
        var checkThis = "b" + i.toString();
        if (divid == checkThis) {
            arrayXO[i-1] = turnString;
            console.log(arrayXO);
        }
    }
    return arrayXO;
}


function computerUpdateArray(divid, turnString){
    for (var i = 1; i < 10; i++){
        var checkThis = "b" + i.toString();
        if (divid == checkThis) {
            arrayXO[i-1] = turnString;
            console.log(arrayXO);
        }
    }
}


function changeXO(divid){
    var contents = document.createElement("p");
    if (turn % 2 == 0){
        var dummyArray = updateArray(divid, "X");
        contents.innerHTML = "X";
    } else {
        var dummyArray = updateArray(divid, "O");
        contents.innerHTML = "O";
    }
    document.getElementById(divid).appendChild(contents);
    document.getElementById(divid).onclick = null;
    turn++;
    var winDummy = checkWin(dummyArray, turn);
    if (winDummy == "endingSequence") {
        lockBoard(winDummy);
        winSequence();
    } else {
        computerChangeXO(dummyArray);
    }
}


function computerChangeXO(arrayXO){
    var dummyChoice = computerChooses(arrayXO);
    var contents = document.createElement("p");
    if (turn % 2 == 0){
        computerUpdateArray(dummyChoice, "X");
        contents.innerHTML = "X";
    } else {
        computerUpdateArray(dummyChoice, "O");
        contents.innerHTML = "O";
    }
    document.getElementById(dummyChoice).appendChild(contents);
    document.getElementById(dummyChoice).onclick = null;
    turn++;
    var winDummy = checkWin(arrayXO, turn);
    if (winDummy == "endingSequence") {
        lockBoard(winDummy);
        winSequence();
    }
}


function computerChooses(someArray) {
    // search randomly from arrayXO to pick a line that is "*"
    var isValidGuess = false;
    while (isValidGuess == false) {
        var arrayIndex = Math.floor(((Math.random() * someArray.length) + 1) - 1);
        var computerGuess = someArray[arrayIndex];
        arrayIndex += 1; // to convert from programmer counting to normal counting
        if (computerGuess == "*") {
            isValidGuess = true;
            var boxSelected = "b" + arrayIndex.toString();
            console.log(boxSelected);
            break;
        }
    }
    return boxSelected;
}


function checkWin(theArray, turn) {
    var gameOver = "no";

    if (theArray[0] == theArray[1] && theArray[1] == theArray[2] && theArray[1] != "*"){
        gameOver = "yes";
        // console.log("1");
    } else if (theArray[3] == theArray[4] && theArray[4] == theArray[5] && theArray[4] != "*"){
        gameOver = "yes";
        // console.log("2");
    } else if (theArray[6] == theArray[7] && theArray[7] == theArray[8] && theArray[7] != "*"){
        gameOver = "yes";
        // console.log("3");
    } else if (theArray[0] == theArray[3] && theArray[3] == theArray[6] && theArray[3] != "*"){
        gameOver = "yes";
        // console.log("4");
    } else if (theArray[1] == theArray[4] && theArray[4] == theArray[7] && theArray[4] != "*"){
        gameOver = "yes";
        // console.log("5");
    } else if (theArray[2] == theArray[5] && theArray[5] == theArray[8] && theArray[5] != "*"){
        gameOver = "yes";
        // console.log("6");
    } else if (theArray[0] == theArray[4] && theArray[4] == theArray[8] && theArray[4] != "*"){
        gameOver = "yes";
        // console.log("7");
    } else if (theArray[2] == theArray[4] && theArray[4] == theArray[6] && theArray[4] != "*"){
        gameOver = "yes";
        // console.log("8");
    } else if (theArray.includes("*")){
        gameOver = "no";
        // console.log("9");
    } else {
        gameOver = "tie";
        // console.log("10");
    }

    if (gameOver == "tie"){
        var tieGame = document.createElement("p");
        tieGame.innerHTML = "It is a Tie!";
        document.getElementById("theContainer").appendChild(tieGame);
        return "endingSequence";
    } else if (gameOver == "yes"){
        var winnerIs = document.createElement("p");
        if (turn % 2 == 0) {
            winnerIs.innerHTML = "O's win!";
            document.getElementById("theContainer").appendChild(winnerIs);
        } else {
            winnerIs.innerHTML = "X's win!";
            document.getElementById("theContainer").appendChild(winnerIs);
        }
        return "endingSequence";
    } else {
        return null;
    }
}


function lockBoard(endit) {
    if (endit == "endingSequence"){
        document.getElementById("b1").onclick = null;
        document.getElementById("b2").onclick = null;
        document.getElementById("b3").onclick = null;
        document.getElementById("b4").onclick = null;
        document.getElementById("b5").onclick = null;
        document.getElementById("b6").onclick = null;
        document.getElementById("b7").onclick = null;
        document.getElementById("b8").onclick = null;
        document.getElementById("b9").onclick = null;
    }
}


function winSequence() {
    var winStatement = document.createElement("p");
    winStatement.innerHTML = "Game Over!";
    document.getElementById("theContainer").appendChild(winStatement);
    document.getElementById("turnSignifier").style.visibility = "hidden";
    document.getElementById("restartButton").style.visibility = "visible";
}


function restarting() {
    location.reload();
}