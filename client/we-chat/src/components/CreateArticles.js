import React from "react";
import {Form, Button} from 'react-bootstrap'
import {useForm} from 'react-hook-form'

const CreateArticle =()=>{

    const {register,handleSubmit, reset, formState:{errors}}= useForm()

    const createArticle=(data)=>{
        console.log(data)

    const requestOptions={
        method:'POST',
        headers:{
            'content-type': 'application/json',
        },
        body: JSON.stringify(data)
    }

    fetch('http://127.0.0.1:5000/add_article',requestOptions)
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
        reset()
    })
    .catch(err=>console.log(err))
    }
    return(
        <div className="container">
            <h1>Create A New Article</h1>
            <form>
                <Form.Group>
                    <Form.Label>Title</Form.Label>
                    <Form.Control type="text"
                      {...register('title',{required:true, maxLength: 20})}
                    />
                </Form.Group>
                {errors.title && <p  style={{color:'red'}}><small>Title is required</small></p>}
                {errors.title?.type ==="maxLength" && <p style={{color:'red'}}><small>Title length should not exceed 20 characters</small></p>}
                <Form.Group>
                    <Form.Label>Body</Form.Label>
                    <Form.Control as="textarea" rows={5}
                      {...register('body',{required: true, maxLength:200})}
                    />
                </Form.Group>
                {errors.body && <p  style={{color:'red'}}><small>Article body is required</small></p>}
                {errors.title?.type ==="maxLength" && <p style={{color:'red'}}><small>Article body should not exceed 200 characters</small></p>}
                <Form.Group>
                    <Form.Label>created_at</Form.Label>
                    <Form.Control type="date"
                       {...register('date', {required: false})}
                     />
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Button variant="primary" onClick={handleSubmit(createArticle)}>Submit</Button>
                </Form.Group>
                
            </form>
        </div>
    )
}
export default CreateArticle