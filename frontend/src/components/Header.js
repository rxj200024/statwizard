import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const HeaderContainer = styled.header`
  background-color: #33424A;
  color: #D3D3D3;
  padding: 0.8rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 102%;
  top: 0;
  z-index: 1000;
  margin-top: -9px;
  margin-left: -20px;
`;

const Title = styled.h1`
  margin-left: 20px;
  margin-right: 0;
  margin-top: 0;
  margin-bottom: 0;
`;

const ButtonContainer = styled.div`
  display: flex;
`;

const Button = styled.button`
  background-color: #fff;
  color: black;
  padding: 0.5rem 1rem;
  margin-left: 0.5rem;
  margin-right: 0.5rem;
  border: rounded;
  border-radius: 3px;
  cursor: pointer;
`;

const Header = () => {
  return (
    <HeaderContainer className='border-2 border-black'>
      <Title className="font-serif text-2xl">statwizard</Title>
      <ButtonContainer>
        <Link to="/"><Button className='font-serif text-sm outline outline-offset-1 outline-black'>Home</Button></Link>
        <Button className='font-serif text-sm outline outline-offset-1 outline-black'>About Us</Button>
      </ButtonContainer>  
    </HeaderContainer>
  );
};

export default Header;
