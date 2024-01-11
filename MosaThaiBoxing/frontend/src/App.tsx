import * as React from 'react';
import './styles/App.css';
import  Header  from './components/Header'
import MainPage from "./components/Main/MainPage";


const App: React.FC = () => {
    return (
        <div className="container">
            <header>
                <Header/>
            </header>
            <main>
                <MainPage/>
            </main>
            <footer>
            </footer>
        </div>
    );
};

export default App;