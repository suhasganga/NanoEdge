import { Component } from "solid-js";
import {
  ContextMenu,
  ContextMenuCheckboxItem,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuRadioGroup,
  ContextMenuRadioItem,
  ContextMenuSeparator,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuTrigger,
} from "./ui/ContextMenu";
import {
  settings,
  updateSetting,
  PriceScaleMode,
} from "~/stores/chartSettings";

/**
 * ChartContextMenu
 *
 * TradingView-style right-click context menu for chart settings.
 * Provides quick access to scale modes, price labels, and settings.
 */

interface ChartContextMenuProps {
  children: any; // The chart element to wrap
  onOpenSettings?: () => void;
}

export const ChartContextMenu: Component<ChartContextMenuProps> = (props) => {
  const currentSettings = settings;

  // Handlers
  const handleAutoScaleToggle = (checked: boolean) => {
    updateSetting("autoScale", checked);
  };

  const handleLockRatioToggle = (checked: boolean) => {
    updateSetting("lockPriceToBarRatio", checked);
  };

  const handleInvertScaleToggle = (checked: boolean) => {
    updateSetting("invertScale", checked);
  };

  const handleScaleModeChange = (value: string) => {
    updateSetting("scaleMode", parseInt(value) as PriceScaleMode);
  };

  const handlePriceScalePositionToggle = () => {
    updateSetting(
      "priceScalePosition",
      currentSettings().priceScalePosition === "right" ? "left" : "right"
    );
  };

  // Price labels handlers
  const handleShowLastPriceToggle = (checked: boolean) => {
    updateSetting("showLastPriceLine", checked);
  };

  const handleShowPrevDayCloseToggle = (checked: boolean) => {
    updateSetting("showPrevDayClose", checked);
  };

  const handleShowHighLowToggle = (checked: boolean) => {
    updateSetting("showHighLowLines", checked);
  };

  const handleShowBidAskToggle = (checked: boolean) => {
    updateSetting("showBidAskLines", checked);
  };

  // Grid handlers
  const handleGridVerticalToggle = (checked: boolean) => {
    updateSetting("gridVerticalVisible", checked);
  };

  const handleGridHorizontalToggle = (checked: boolean) => {
    updateSetting("gridHorizontalVisible", checked);
  };

  return (
    <ContextMenu.Root>
      <ContextMenuTrigger class="w-full h-full">
        {props.children}
      </ContextMenuTrigger>

      <ContextMenuContent>
        {/* Auto (fits data to screen) */}
        <ContextMenuCheckboxItem
          checked={currentSettings().autoScale}
          onChange={handleAutoScaleToggle}
        >
          Auto (fits data to screen)
        </ContextMenuCheckboxItem>

        <ContextMenuSeparator />

        {/* Lock price to bar ratio */}
        <ContextMenuCheckboxItem
          checked={currentSettings().lockPriceToBarRatio}
          onChange={handleLockRatioToggle}
        >
          Lock price to bar ratio
        </ContextMenuCheckboxItem>

        {/* Invert scale */}
        <ContextMenuCheckboxItem
          checked={currentSettings().invertScale}
          onChange={handleInvertScaleToggle}
          shortcut="Alt + I"
        >
          Invert scale
        </ContextMenuCheckboxItem>

        <ContextMenuSeparator />

        {/* Scale modes */}
        <ContextMenuRadioGroup
          value={String(currentSettings().scaleMode)}
          onChange={handleScaleModeChange}
        >
          <ContextMenuRadioItem value="0">Regular</ContextMenuRadioItem>
          <ContextMenuRadioItem value="2" shortcut="Alt + P">
            Percent
          </ContextMenuRadioItem>
          <ContextMenuRadioItem value="3">Indexed to 100</ContextMenuRadioItem>
          <ContextMenuRadioItem value="1" shortcut="Alt + L">
            Logarithmic
          </ContextMenuRadioItem>
        </ContextMenuRadioGroup>

        <ContextMenuSeparator />

        {/* Move scale to left/right */}
        <ContextMenuItem onSelect={handlePriceScalePositionToggle}>
          Move scale to {currentSettings().priceScalePosition === "right" ? "left" : "right"}
        </ContextMenuItem>

        <ContextMenuSeparator />

        {/* Labels submenu */}
        <ContextMenuSub>
          <ContextMenuSubTrigger>Labels</ContextMenuSubTrigger>
          <ContextMenuSubContent>
            <ContextMenuCheckboxItem
              checked={currentSettings().showLastPriceLine}
              onChange={handleShowLastPriceToggle}
            >
              Symbol value
            </ContextMenuCheckboxItem>
            <ContextMenuCheckboxItem
              checked={currentSettings().showPrevDayClose}
              onChange={handleShowPrevDayCloseToggle}
            >
              Previous day close
            </ContextMenuCheckboxItem>
            <ContextMenuCheckboxItem
              checked={currentSettings().showHighLowLines}
              onChange={handleShowHighLowToggle}
            >
              High/Low
            </ContextMenuCheckboxItem>
            <ContextMenuCheckboxItem
              checked={currentSettings().showBidAskLines}
              onChange={handleShowBidAskToggle}
            >
              Bid/Ask
            </ContextMenuCheckboxItem>
          </ContextMenuSubContent>
        </ContextMenuSub>

        {/* Lines submenu */}
        <ContextMenuSub>
          <ContextMenuSubTrigger>Lines</ContextMenuSubTrigger>
          <ContextMenuSubContent>
            <ContextMenuCheckboxItem
              checked={currentSettings().gridVerticalVisible}
              onChange={handleGridVerticalToggle}
            >
              Vertical grid lines
            </ContextMenuCheckboxItem>
            <ContextMenuCheckboxItem
              checked={currentSettings().gridHorizontalVisible}
              onChange={handleGridHorizontalToggle}
            >
              Horizontal grid lines
            </ContextMenuCheckboxItem>
          </ContextMenuSubContent>
        </ContextMenuSub>

        <ContextMenuSeparator />

        {/* Settings */}
        <ContextMenuItem onSelect={props.onOpenSettings}>
          Settings...
        </ContextMenuItem>
      </ContextMenuContent>
    </ContextMenu.Root>
  );
};
