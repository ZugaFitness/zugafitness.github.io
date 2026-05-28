import { test, expect } from '@playwright/test';
import path from 'path';

test('verify root page', async ({ page }) => {
  const filePath = `file://${path.resolve('corporate-yoga-day-bangalore.html')}`;
  await page.goto(filePath);
  await page.screenshot({ path: 'verification/root_page.png', fullPage: false });
});
