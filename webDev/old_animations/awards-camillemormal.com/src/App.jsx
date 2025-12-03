import { useState } from 'react'
import './App.css'
import { Route, BrowserRouter as Router, Routes, useLocation } from "react-router-dom"
import { AnimatePresence } from "framer-motion";
import Header from './components/header';
import Track from './components/image-track';
import About from './components/about';
function App() {
  
 
  return (
    <div className='main'>
      <Header/>
      <AnimatePresence mode="wait">
        
          <Routes location = {location} key={location.key}>
            <Route path="/" element={<Track/>}/>
            <Route path="/about" element={<About/>}/>
          </Routes>
        
      </AnimatePresence>
    </div>
  )
}

export default App
