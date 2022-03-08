import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import './InputBar.css';

function InputBar() {

  const [todo, setTodo] = useState("");
  const [list, setList] = useState([]);

  const addTodo = (e) => {
    if (!todo) {
      alert("Enter A URL");
    }
    else {
      e.preventDefault();
      setList(...list, todo);
      setTodo("");
    }
  };


  return (
    <>
      <div className='Search'>
        <Form>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Control type="text" placeholder="Paste Video link" value={todo} onChange={(e) => setTodo(e.target.value)} />
          </Form.Group>

          <Button className="button" variant="primary" type="submit" onClick={addTodo}>
            Submit
          </Button>
        </Form>
      </div>
    </>
  )
}

export default InputBar