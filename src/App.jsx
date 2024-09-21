import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Button } from 'primereact/button';
import Login from './components/lgin/login';
import FaceDetection from './components/faceDetection';
function App() {
  const [count, setCount] = useState(0)
  const [name , setName] = useState( "usman" )
  
  console.log(name)
  // console.log(state)
  // let name = "usman"

  // name = "ahmed"
  return (
    <>
    <div style={{border:"solid"}}>
  {/* {setName("ahmed")} */}
       <Login  c="read-the-docs" />
       <div ></div>
       <Button label="Check" icon="pi pi-check"  onClick={() => setName("ahmed")}/>
       </div>
         <FaceDetection />
           </>
  )
}

export default App
