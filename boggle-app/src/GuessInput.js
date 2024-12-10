import React, { useState } from 'react';
import TextField from "@material-ui/core/TextField";
import './GuessInput.css';

function GuessInput({allSolutions, foundSolutions, correctAnswerCallback}) {

  const [labelText, setLabelText] = useState("Make your first guess!");
  const [input, setInput] = useState("");
  
  function evaluateInput() {
    if (foundSolutions.includes(input.toUpperCase())) {
      setLabelText(input + " has already been found!");
    } else if (allSolutions.includes(input.toLowerCase())) {
      correctAnswerCallback(input.toUpperCase());
      setLabelText(input + " is correct!");
    } else {
      setLabelText(input + " is incorrect!");
    }

  }

  function keyPress(e) {
    if (e.key === 'Enter') {
      e.target.value = "";
      evaluateInput()
    }
  }

  return (
    <div className="Guess-input">
      <div>
        {labelText}
      </div>
      <TextField onKeyPress={(e) => keyPress(e)} onChange={(event) => setInput(event.target.value.toUpperCase())} />
    </div>
  );
}

export default GuessInput;
