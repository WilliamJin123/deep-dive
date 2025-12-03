import { useState } from 'react'
import Carousel from './components/carousel'
import './App.css'

function App() {
  
  return (
    <div className='main'>
      <div className='block'>scroll down</div>
      <Carousel/>
      <div className='block'>scroll up</div>
    </div>
  )
}

export default App
