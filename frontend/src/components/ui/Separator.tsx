import { Component, JSX, splitProps } from "solid-js";
import { cn } from "~/lib/utils";

interface SeparatorProps extends JSX.HTMLAttributes<HTMLDivElement> {
  orientation?: "horizontal" | "vertical";
}

export const Separator: Component<SeparatorProps> = (props) => {
  const [local, others] = splitProps(props, ["class", "orientation"]);
  const orientation = () => local.orientation ?? "horizontal";

  return (
    <div
      role="separator"
      aria-orientation={orientation()}
      class={cn(
        "shrink-0 bg-[#2a2e39]",
        orientation() === "horizontal" ? "h-px w-full my-1" : "w-px h-full mx-1",
        local.class
      )}
      {...others}
    />
  );
};
