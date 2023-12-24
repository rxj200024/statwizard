import React from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer';
import { Button } from '@mui/material';
import PlayerDropdown from '../components/PlayerDropdown';



const Home = () => {
  return (
    <>
      <Header/>
      <div style={{height: '70vh'}} className="flex flex-col items-center justify-center h-screen ">
        <PlayerDropdown/>
      </div>
      <Footer/>
    </>
  )
}

export default Home
