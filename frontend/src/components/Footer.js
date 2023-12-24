import React from 'react';
import styled from 'styled-components';

const FooterContainer = styled.footer`
  background-color: #33424A;
  color: #D3D3D3;
  padding: 0.8rem;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  position: fixed;
  bottom: 0;
`;

const CopyrightText = styled.p`
  margin: 0;
  font-size: 12px;
`;

const Footer = () => {
  return (
    <FooterContainer>
      <CopyrightText>&copy; 2023 statwizard. All rights reserved.</CopyrightText>
    </FooterContainer>
  );
};

export default Footer;