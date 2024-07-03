import { CoursePurchaseCard } from "@/components/CoursePurchaseCard";
import { GetInTouch } from "@/components/GetInTouch";
import Image from "next/image";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-between gap-4 p-24">
      <CoursePurchaseCard />
      <GetInTouch/>
    </main>
  );
}
