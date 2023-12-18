import React from "react";
import {Card} from 'react-bootstrap'

const Article =({title, body, created_at, updated_at})=>{
    return(
        <div className="article">
            <Card className="article">
                <Card.Body>
                <Card.Title>{title}</Card.Title>
                <p>{body}</p>
                <p>{created_at}</p>
                <p>{updated_at}</p>  
                </Card.Body>
            </Card>
        </div>
    )
}
export default Article
