// pages/index.tsx
export default function Home() {
  return (
    <div className="min-h-[100svh] bg-gradient-to-b from-white to-gray-50 text-gray-900">
      <header className="w-full">
        <div className="mx-auto max-w-6xl px-4 py-6 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="h-7 w-7 rounded bg-gray-900"></div>
            <span className="text-lg font-semibold tracking-tight bg-gradient-to-r from-purple-600 via-fuchsia-500 to-amber-400 bg-clip-text text-transparent">
              Next Role
            </span>
          </div>
          <nav className="flex items-center gap-6 text-sm text-gray-600">
            <a href="#features" className="hover:text-gray-900">
              Features
            </a>
            <a href="#how" className="hover:text-gray-900">
              How it works
            </a>
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-4">
        <section className="relative pt-16 pb-16 sm:pt-14 sm:pb-28">
          <div className="pointer-events-none absolute inset-0 -z-10 [mask-image:radial-gradient(40rem_40rem_at_center,black,transparent)]">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(59,130,246,0.07),transparent_50%)]"></div>
          </div>

          <div className="mx-auto max-w-3xl text-center">
            <h1 className="text-4xl sm:text-5xl font-semibold tracking-tight leading-tight">
              Find careers that match your skills
            </h1>
            <p className="mt-4 text-base sm:text-lg text-gray-600">
              Enter a skill and instantly get role suggestions, required skills,
              and companies hiring for them.
            </p>
          </div>

          <div className="mx-auto mt-10 max-w-xl">
            <form className="group rounded-xl border border-gray-200 bg-white/70 backdrop-blur px-3 py-2 shadow-sm focus-within:ring-2 focus-within:ring-gray-900/5">
              <div className="flex items-center gap-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.5"
                  className="h-5 w-5 text-gray-400"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="m21 21-4.3-4.3M11 18a7 7 0 1 1 0-14 7 7 0 0 1 0 14Z"
                  />
                </svg>
                <input
                  type="text"
                  placeholder="Try “Python”, “UX Design”, “Data Analysis”"
                  className="w-full bg-transparent outline-none placeholder:text-gray-400 text-sm sm:text-base"
                />
                <button
                  type="submit"
                  className="cursor-pointer shrink-0 rounded-lg bg-gradient-to-r from-purple-600 via-fuchsia-500 to-amber-400 px-5 py-2.5 text-sm font-medium text-white transition hover:from-purple-700 hover:via-fuchsia-600 hover:to-amber-500"
                >
                  Explore
                </button>
              </div>
            </form>
            <div className="mt-3 flex flex-wrap items-center gap-2 text-xs text-gray-500">
              <span>Popular:</span>
              <button className="rounded-full border border-gray-200 px-3 py-1 hover:border-gray-300">
                JavaScript
              </button>
              <button className="rounded-full border border-gray-200 px-3 py-1 hover:border-gray-300">
                Product Management
              </button>
              <button className="rounded-full border border-gray-200 px-3 py-1 hover:border-gray-300">
                Cloud
              </button>
            </div>
          </div>

          <div
            id="features"
            className="mx-auto mt-16 grid gap-6 sm:grid-cols-3"
          >
            <div className="rounded-xl border border-gray-200 bg-white p-5">
              <div className="text-sm font-medium">Career paths</div>
              <p className="mt-1 text-sm text-gray-600">
                Roles that align with your core skill.
              </p>
            </div>
            <div className="rounded-xl border border-gray-200 bg-white p-5">
              <div className="text-sm font-medium">Required skills</div>
              <p className="mt-1 text-sm text-gray-600">
                What to learn next to be job‑ready.
              </p>
            </div>
            <div className="rounded-xl border border-gray-200 bg-white p-5">
              <div className="text-sm font-medium">Hiring companies</div>
              <p className="mt-1 text-sm text-gray-600">
                Up‑to‑date companies that hire for the role.
              </p>
            </div>
          </div>

          <div
            id="how"
            className="mx-auto mt-12 max-w-2xl text-center text-sm text-gray-500"
          >
            Paste a skill above and we’ll use our backend LLM to generate role
            ideas, the skill gaps to close, and a list of companies frequently
            hiring.
          </div>
        </section>
      </main>

      <footer className="border-t border-gray-100">
        <div className="mx-auto max-w-6xl px-4 py-8 text-xs text-gray-500 flex items-center justify-center">
          <span>© {new Date().getFullYear()} Next Role</span>
        </div>
      </footer>
    </div>
  );
}
