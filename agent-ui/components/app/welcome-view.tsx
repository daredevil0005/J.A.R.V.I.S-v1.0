'use client';

import { motion } from 'motion/react';
import { Button } from '@/components/ui/button';

function WelcomeImage() {
  return (
    <motion.img
      src="/ironman.jpg"
      alt="J.A.R.V.I.S."
      width={160}
      height={160}
      className="mb-4 block shrink-0 object-cover"
      loading="eager"
      fetchPriority="high"
      initial={{ opacity: 0, scale: 0.7 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{
        duration: 0.6,
        ease: [0.34, 1.56, 0.64, 1],
        delay: 0.15,
      }}
    />
  );
}

interface WelcomeViewProps {
  startButtonText: string;
  onStartCall: () => void;
}

export const WelcomeView = ({
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeViewProps) => {
  return (
    <div ref={ref} className="relative z-20 flex min-h-[50vh] w-full items-center justify-center">
      <section className="flex flex-col items-center justify-center text-center bg-transparent">
        <WelcomeImage />

        <p className="text-foreground max-w-prose pt-1 leading-6 font-medium">
          Chat With Advanced AI Assistant
        </p>

        <Button
          size="lg"
          onClick={onStartCall}
          className="mt-6 w-64 rounded-full font-mono text-xs font-bold tracking-wider uppercase"
        >
          {startButtonText}
        </Button>
      </section>
    </div>
  );
};
