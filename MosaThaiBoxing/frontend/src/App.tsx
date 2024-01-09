import * as React from 'react';
// @ts-ignore
import main from '@images/main.png';

const App: React.FC = () => {
    return (
        <div className="container">
            <header>
               header
            </header>
            <main>
                <img src={main} alt="main picture"/>
                main
            </main>
            <footer>
                footer
            </footer>
        </div>
    );
};

export default App;
