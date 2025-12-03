import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import SpaceshipParallax from './Spaceship-Parallax'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <SpaceshipParallax />
  </StrictMode>,
)
