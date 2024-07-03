"use client"
import { cn } from "@/lib/utils";
import { useEffect } from "react";
import { buttonVariants } from "./ui/button";

export function CoursePurchaseCard() {
  const emitEvent = (eventName: string) => {
    fetch('http://localhost:8000/product/event', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ event: eventName }),
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('failed')
        }
      })
      .catch(error => {
        console.error('Error emitting event: ', error);
      })
  };

  const handleBuyCourseClick = () => {
    emitEvent("userClickEnrollNow");
  };

  return (
    <div className="flex flex-col gap-4">
      <span className="text-3xl">Welcome to course Platform</span>
      <div
        onClick={handleBuyCourseClick}
        className={cn(
          buttonVariants({ variant: "default" }),
          "hidden sm:inline-flex hover:cursor-pointer"
        )}
      >
        <span className="text-xl font-semibold">Buy a course</span>
      </div>
    </div>
  )
}
