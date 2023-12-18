
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import NavBar from './components/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css'

import{BrowserRouter, Routes, Route} from 'react-router-dom'
import CreateArticle from './components/CreateArticles';
import ContactUs from './components/ContactUs';
import Home from './components/Home';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
  <React.StrictMode>
    <App />
    <NavBar/>
    <Routes>
      <Route path="/create_article" element={<CreateArticle/>} />
      <Route path="/contact_us" element={<ContactUs/>} />
      <Route path="/" element={<Home/>} />
    </Routes>
  </React.StrictMode>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
