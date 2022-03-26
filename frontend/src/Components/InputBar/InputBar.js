import React, { useState, Component } from 'react';
import { Button, Form } from 'react-bootstrap';
import Async from 'react-async';
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

  function componentDidMount() {
    fetch("http://localhost:8000/url/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

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

        <ul>
        {this.state.data.map(url => {
          return (
            <li >
              {input_url}
            </li>
          );
        })}
      </ul>
      </div>
    </>
  )
}

export default InputBar