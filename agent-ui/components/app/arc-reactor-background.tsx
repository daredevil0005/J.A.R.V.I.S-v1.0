'use client';

export function ArcReactorBackground() {
  return (
    <div
      className="fixed inset-0 z-0 overflow-hidden"
      aria-hidden
    >
      {/* Dark base layer - darker than reference image */}
      <div
        className="absolute inset-0"
        style={{
          background:
            'radial-gradient(ellipse 120% 100% at 50% 50%, rgba(5, 10, 25, 0.98) 0%, rgba(0, 2, 8, 0.99) 50%, #000 100%)',
        }}
      />

      {/* Blurred Arc Reactor and UI elements */}
      <div
        className="absolute inset-0 flex items-center justify-center"
        style={{ filter: 'blur(32px)', opacity: 0.9 }}
      >
        {/* Central Arc Reactor glow */}
        <div className="relative">
          {/* Outer ring - rotating */}
          <div
            className="absolute left-1/2 top-1/2 h-[320px] w-[320px] -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-cyan-500/60"
            style={{
              animation: 'arc-rotate 8s linear infinite',
              willChange: 'transform',
              boxShadow: '0 0 60px rgba(34, 211, 238, 0.3), inset 0 0 40px rgba(34, 211, 238, 0.1)',
            }}
          />
          {/* Middle ring */}
          <div
            className="absolute left-1/2 top-1/2 h-[220px] w-[220px] -translate-x-1/2 -translate-y-1/2 rounded-full border border-cyan-400/50"
            style={{
              animation: 'arc-rotate 12s linear infinite reverse',
              boxShadow: '0 0 40px rgba(34, 211, 238, 0.25)',
            }}
          />
          {/* Inner core - pulsing */}
          <div
            className="absolute left-1/2 top-1/2 h-[120px] w-[120px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-400/40"
            style={{
              animation: 'arc-pulse 2s ease-in-out infinite',
              boxShadow: '0 0 80px rgba(34, 211, 238, 0.5), inset 0 0 30px rgba(34, 211, 238, 0.3)',
            }}
          />
          {/* Central triangle/core */}
          <div
            className="absolute left-1/2 top-1/2 h-[40px] w-[40px] -translate-x-1/2 -translate-y-1/2 bg-cyan-300/70"
            style={{
              clipPath: 'polygon(50% 0%, 100% 100%, 0% 100%)',
              animation: 'arc-pulse 1.5s ease-in-out infinite',
              boxShadow: '0 0 30px rgba(34, 211, 238, 0.8)',
            }}
          />
        </div>

        {/* Left UI bar */}
        <div
          className="absolute left-[8%] top-1/2 h-3 w-32 -translate-y-1/2 rounded-full border border-cyan-500/40 bg-cyan-950/30"
          style={{
            animation: 'arc-scan 3s ease-in-out infinite',
            boxShadow: '0 0 20px rgba(34, 211, 238, 0.2)',
          }}
        />
        {/* Right UI bar */}
        <div
          className="absolute right-[8%] top-1/2 h-3 w-32 -translate-y-1/2 rounded-full border border-cyan-500/40 bg-cyan-950/30"
          style={{
            animation: 'arc-scan 3s ease-in-out infinite 1.5s',
            boxShadow: '0 0 20px rgba(34, 211, 238, 0.2)',
          }}
        />

        {/* Radial red accent lines */}
        <div
          className="absolute left-1/2 top-1/2 h-[400px] w-[400px] -translate-x-1/2 -translate-y-1/2 rounded-full border border-red-500/20"
          style={{ animation: 'arc-rotate 20s linear infinite' }}
        />
        <div
          className="absolute left-1/2 top-1/2 h-[380px] w-[380px] -translate-x-1/2 -translate-y-1/2 rounded-full border border-red-600/15"
          style={{ animation: 'arc-rotate 25s linear infinite reverse' }}
        />
      </div>

      {/* Subtle geometric grid overlay */}
      <div
        className="pointer-events-none absolute inset-0 opacity-[0.03]"
        style={{
          backgroundImage: `
            linear-gradient(rgba(34, 211, 238, 0.5) 1px, transparent 1px),
            linear-gradient(90deg, rgba(34, 211, 238, 0.5) 1px, transparent 1px)
          `,
          backgroundSize: '40px 40px',
        }}
      />
    </div>
  );
}
