import "./globals.css";

export const metadata = {
  title: "GraveyAI",
  description: "AI knowledge and assistance platform powered by GraveyChain.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
