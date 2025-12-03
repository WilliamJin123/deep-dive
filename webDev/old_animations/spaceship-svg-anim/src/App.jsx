import { useState } from 'react'
import { SpaceShipSvg } from './components/spaceshipSvg'
import './App.css'


function App() {
  
  return (
    <div className='main'>
      <div className='spaceship'>
         <SpaceShipSvg/>
      </div>
      <div className='header'>Aliens are coming</div>
    </div>
  )
}

export default App
