import styled from 'styled-components'

export const MetaContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

`

export const MediumContainer = styled.div`
  max-width: 1024px;
  position: relative;
  display: grid;
  width: 100%;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center;
  padding: 60px 20px;
`

export const AboutDescription = styled.div`
  position: relative;
  display: grid;
  width: 100%;
  backgroundcolor: "green";
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  justify-content: center;
  align-content: center;
  padding: 100px 0px;
`

export const Header1 = styled.h1`
    color: #4f5d75;
`

export const Details = styled.p`
    margin: 2rem 0;
    color: rgba(43,46,50,.85);
    line-height: 1.5715;
    text-align: center;
`

export const HeaderImage = styled.img`
  width: 100%;
  max-width: 400px;
  height: auto;
  align-self: center;
  justify-self: center;
  padding: 20px;
`

export const Button = styled.button`
    padding: 8px 20px;
    border-radius: 4px;
    background-color: #008080;
    border: none;
    color: #ffffff;
    font-size: 16px;
    box-shadow: 0 2px 0 rgba(0,0,0,.045);
    height: 40px;
    font-weight: 600;

    & a{
      text-decoration: none;
      color: #ffffff;
    }
  `

  export const Container = styled.div`
      width: 90%;
      margin: auto;
      justify-content: center;
      margin-bottom: 20px;
      display: flex;
  `

  export const Input = styled.input`
    width: 70%;
    margin-bottom: 10px;
    background-color: #fff;
    padding: 0.75rem 0 0.75rem 1rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #8492a6;
    transition: 0.2s;
    box-shadow: none;
    border: 1px solid #e0e6ed;
    border-radius: 0.25rem;
    font-family: 'Inter', sans-serif;


    &:focus {
      outline: 0;
      border-color: #008080;
      box-shadow: 0 0 1.25rem rgba(31, 45, 61, 0.08);
    }
  `;


  export const TextArea = styled.textarea`
    width: 100%;
    height: 200px;
    border: 1px solid black;
    font-family: 'Inter', sans-serif;
    background-color: #F4F4F1;
    border-radius: 5px;
    padding: 0.5rem;
    transition: 0.2s;

    &:focus {
      outline: 0;
      border-color: #ffffff;
      box-shadow: 0 0 1.25rem rgba(31, 45, 61, 0.08);
    }
    `
