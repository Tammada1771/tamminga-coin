import React, { useEffect, useState } from "react";

function Joke() {
    const [joke, setJoke] = useState({});

    useEffect(() => {
        fetch('http://localhost:3005/jokes/random')
            .then(response => response.json())
            .then(json => {
                console.log('joke json', json);

                setJoke(json);
            });

        console.log('fetching data');
    }, []);

    const { setup, punchline } = joke

    return (
        <div>
            <h3>Joke</h3>
            <p>{setup}</p>
            <p><em>{punchline}</em></p>
        </div>
    )
}

export default Joke;