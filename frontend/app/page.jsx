"use client";

import { useState } from "react";

const Home = () => {
  const [response, setResponse] = useState("Hello");

  const handleTestBackend = async () => {
    console.log("clicked");

    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/hello`);
    console.log(res);

    if (res.ok) {
      const data = await res.json();
      setResponse(data.message);
    }
  };
  return (
    <main className="h-screen flex items-center justify-center">
      <div className="flex items-center justify-center flex-col gap-4">
        <h1>{response}</h1>
        <button
          onClick={handleTestBackend}
          className="py-2 px-4 bg-zinc-100 rounded-md text-black cursor-pointer"
        >
          Test backend
        </button>
      </div>
    </main>
  );
};

export default Home;
