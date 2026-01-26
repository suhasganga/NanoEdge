import {
  Component,
  JSX,
  splitProps,
  Show,
  ParentComponent,
} from "solid-js";
import { Dialog as KDialog } from "@kobalte/core/dialog";
import { cn } from "~/lib/utils";

// Close icon
const CloseIcon: Component = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="18" height="18">
    <path
      stroke="currentColor"
      stroke-width="1.2"
      d="m1.5 1.5 15 15m0-15-15 15"
    />
  </svg>
);

// Dialog Root
export const DialogRoot = KDialog;

// Dialog Trigger
interface DialogTriggerProps {
  children: JSX.Element;
  class?: string;
}

export const DialogTrigger: ParentComponent<DialogTriggerProps> = (props) => {
  return (
    <KDialog.Trigger class={cn("outline-none", props.class)}>
      {props.children}
    </KDialog.Trigger>
  );
};

// Dialog Portal
export const DialogPortal = KDialog.Portal;

// Dialog Overlay
interface DialogOverlayProps {
  class?: string;
}

export const DialogOverlay: Component<DialogOverlayProps> = (props) => {
  return (
    <KDialog.Overlay
      class={cn(
        "fixed inset-0 z-50 bg-black/50 backdrop-blur-sm",
        "animate-in fade-in-0",
        "data-[state=closed]:animate-out data-[state=closed]:fade-out-0",
        props.class
      )}
    />
  );
};

// Dialog Content
interface DialogContentProps {
  children: JSX.Element;
  class?: string;
  showClose?: boolean;
  onClose?: () => void;
}

export const DialogContent: ParentComponent<DialogContentProps> = (props) => {
  const [local] = splitProps(props, ["children", "class", "showClose", "onClose"]);

  return (
    <KDialog.Portal>
      <DialogOverlay />
      <KDialog.Content
        class={cn(
          "fixed left-1/2 top-1/2 z-50 -translate-x-1/2 -translate-y-1/2",
          "w-full max-w-[600px] max-h-[90vh]",
          "bg-[#1e222d] border border-[#2a2e39] rounded-lg",
          "shadow-[0_4px_20px_rgba(0,0,0,0.4)]",
          "text-[#d1d4dc]",
          "animate-in fade-in-0 zoom-in-95",
          "data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95",
          "outline-none",
          local.class
        )}
      >
        {local.children}
        <Show when={local.showClose !== false}>
          <KDialog.CloseButton
            class={cn(
              "absolute right-3 top-3 p-1.5 rounded",
              "text-[#787b86] hover:text-[#d1d4dc] hover:bg-[#2a2e39]",
              "transition-colors outline-none",
              "focus:ring-1 focus:ring-[#2962ff]"
            )}
            onClick={local.onClose}
          >
            <CloseIcon />
          </KDialog.CloseButton>
        </Show>
      </KDialog.Content>
    </KDialog.Portal>
  );
};

// Dialog Header
interface DialogHeaderProps {
  children: JSX.Element;
  class?: string;
}

export const DialogHeader: ParentComponent<DialogHeaderProps> = (props) => {
  return (
    <div
      class={cn(
        "flex items-center px-4 py-3 border-b border-[#2a2e39]",
        props.class
      )}
    >
      {props.children}
    </div>
  );
};

// Dialog Title
interface DialogTitleProps {
  children: JSX.Element;
  class?: string;
}

export const DialogTitle: ParentComponent<DialogTitleProps> = (props) => {
  return (
    <KDialog.Title
      class={cn("text-[15px] font-medium text-[#d1d4dc]", props.class)}
    >
      {props.children}
    </KDialog.Title>
  );
};

// Dialog Description
interface DialogDescriptionProps {
  children: JSX.Element;
  class?: string;
}

export const DialogDescription: ParentComponent<DialogDescriptionProps> = (props) => {
  return (
    <KDialog.Description
      class={cn("text-[13px] text-[#787b86]", props.class)}
    >
      {props.children}
    </KDialog.Description>
  );
};

// Dialog Body (scrollable content area)
interface DialogBodyProps {
  children: JSX.Element;
  class?: string;
}

export const DialogBody: ParentComponent<DialogBodyProps> = (props) => {
  return (
    <div
      class={cn(
        "flex-1 overflow-y-auto",
        props.class
      )}
    >
      {props.children}
    </div>
  );
};

// Dialog Footer
interface DialogFooterProps {
  children: JSX.Element;
  class?: string;
}

export const DialogFooter: ParentComponent<DialogFooterProps> = (props) => {
  return (
    <div
      class={cn(
        "flex items-center justify-end gap-2 px-4 py-3 border-t border-[#2a2e39]",
        props.class
      )}
    >
      {props.children}
    </div>
  );
};

// Dialog Close Button
export const DialogClose = KDialog.CloseButton;

// Button component for dialogs
interface ButtonProps extends JSX.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
}

export const Button: Component<ButtonProps> = (props) => {
  const [local, others] = splitProps(props, ["variant", "class", "children"]);
  const variant = () => local.variant ?? "secondary";

  return (
    <button
      class={cn(
        "px-4 py-1.5 text-[13px] font-medium rounded transition-colors outline-none",
        "focus:ring-1 focus:ring-[#2962ff]",
        variant() === "primary"
          ? "bg-[#2962ff] text-white hover:bg-[#1e53e4]"
          : "bg-[#2a2e39] text-[#d1d4dc] hover:bg-[#363a45]",
        local.class
      )}
      {...others}
    >
      {local.children}
    </button>
  );
};

// Export all as a namespace for convenience
export const Dialog = {
  Root: DialogRoot,
  Trigger: DialogTrigger,
  Portal: DialogPortal,
  Overlay: DialogOverlay,
  Content: DialogContent,
  Header: DialogHeader,
  Title: DialogTitle,
  Description: DialogDescription,
  Body: DialogBody,
  Footer: DialogFooter,
  Close: DialogClose,
};
