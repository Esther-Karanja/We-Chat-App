import React, {useEffect, useState} from 'react';
import Article from './Article';

const Home =()=>{
    const[articles, setArticles] =useState([]);

  useEffect( () =>{
    fetch('http://127.0.0.1:5000/articles')
    .then(res => res.json())
    .then(data =>{
      setArticles(data)
    })
    .catch(err =>console.log(err))
  },[])

    return(
        <div className="home-page">
            <h1>Welcome to our Articles Blog</h1>
            {
                articles.map(
                (article)=>(
                <Article key ={article.id} title={article.title} body={article.body} created_at={article.created_at} updated_at={article.updated_at}/>
        ))
      }
        </div>
    )
}
export default Home