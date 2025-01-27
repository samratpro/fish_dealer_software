#!/bin/bash
# Define the paths
SCRIPT_PATH="C:/Users/pc/Desktop/fish_dealer_software/App.py"
ICON_PATH="C:/Users/pc/Desktop/fish_dealer_software/logo.ico"
OUTPUT_DIR="C:/Users/pc/Desktop/fish_dealer_software/dist"
NUITKA_PATH="C:/Users/pc/Desktop/fish_dealer_software/env/Scripts/nuitka.cmd"  # Update this path
# pip install nuitka
# or --mingw64 C:\Users\pc\AppData\Local\Programs\Python\Python312\python.exe   py -3.12 -m venv env
# or --msvc=latest with visual studio installer
# use cli >> set _CL_=/Zm2000  or  set _CL_=/Zm3000
# Nuitka command
"$NUITKA_PATH" \
  --standalone \
  --onefile \
  --mingw64 \
  --windows-icon-from-ico="$ICON_PATH" \
  --include-data-files="$ICON_PATH=logo.ico" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/dashboard.py=dashboard.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/login.py=login.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/models.py=models.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/features/data_save_signals.py=features/data_save_signals.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/features/printmemo.py=features/printmemo.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/forms/add_buyer_form.py=forms/add_buyer_form.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/forms/add_buyer_form_ui.py=forms/add_buyer_form_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/forms/cost_entry.py=forms/cost_entry.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/forms/cost_entry_ui.py=forms/cost_entry_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/forms/usersForm.py=forms/usersForm.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/forms/usersForm_ui.py=forms/usersForm_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/buyerProfiles.py=pages/buyerProfiles.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/buyerProfileView.py=pages/buyerProfileView.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/commissionReportPage.py=pages/commissionReportPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/costExpenseEntryPage.py=pages/costExpenseEntryPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/costReportPage.py=pages/costReportPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/homePage.py=pages/homePage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/loanPage.py=pages/loanPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/memoPage.py=pages/memoPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/payableableReportPage.py=pages/payableableReportPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/receivableReportPage.py=pages/receivableReportPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/sellerProfiles.py=pages/sellerProfiles.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/sellerProfileView.py=pages/sellerProfileView.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/settingsPage.py=pages/settingsPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/pages/usersPage.py=pages/usersPage.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/buyerProfiles_ui.py=ui/buyerProfiles_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/buyerProfileView_ui.py=ui/buyerProfileView_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/commissionReportPage_ui.py=ui/commissionReportPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/costExpenseEntryPage_ui.py=ui/costExpenseEntryPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/costReportPage_ui.py=ui/costReportPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/dashboard_ui.py=ui/dashboard_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/homePage_ui.py=ui/homePage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/loanPage_ui.py=ui/loanPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/login_ui.py=ui/login_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/memoPage_ui.py=ui/memoPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/payableableReportPage_ui.py=ui/payableableReportPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/receivableReportPage_ui.py=ui/receivableReportPage_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/sellerProfiles_ui.py=ui/sellerProfiles_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/sellerProfileView_ui.py=ui/sellerProfileView_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/settings_ui.py=ui/settings_ui.py" \
  --include-data-files="C:/Users/pc/Desktop/fish_dealer_software/ui/usersPage_ui.py=ui/usersPage_ui.py" \
  --enable-plugin=pyqt6 \
  --output-dir="$OUTPUT_DIR" \
  --jobs=2 \
  --lto=no \
  --experimental=use_pefile \
  "$SCRIPT_PATH"

# Check if the build was successful
if [ $? -eq 0 ]; then
  echo "Build successful! Executable is located in $OUTPUT_DIR"
else
  echo "Build failed. Check the output for errors."
fi