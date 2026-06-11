const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const files = [
    'Blog/index.html',
    'Blog/yoga-for-weight-management-7-poses.html',
    'Blog/yoga-for-stress-relief.html',
    'Blog/morning-yoga-routine-for-energy.html'
  ];

  for (const file of files) {
    console.log('Verifying ' + file);
    await page.goto('http://localhost:8000/' + file);
    await page.screenshot({ path: '/home/jules/verification/final_' + file.replace(/\//g, '_') + '.png', fullPage: true });
  }

  await browser.close();
})();
