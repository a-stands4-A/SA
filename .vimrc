set nocompatible
set wrapmargin=8

set nu
set relativenumber
syntax on
filetype off
filetype plugin on
set omnifunc=syntaxcomplete#Complete

set expandtab
set sw=2
set sts=2
set autoindent
set smartindent

set textwidth=80
set colorcolumn=80

set cursorline
set mouse=a

set ignorecase

set clipboard+=unnamedplus


set showmode
set showcmd
set wildmenu
set wildmode=list:longest

" Display different types of white spaces.
set list
set listchars=eol:¬,tab:>·,trail:~,extends:>,precedes:<,space:␣ "set nolist

set hlsearch

" When editing a file, always jump to the last known cursor position.
autocmd BufReadPost *
  \ if line("'\"") >= 1 && line("'\"") <= line("$") && &ft !~# 'commit'
  \ |   exe "normal! g`\""
  \ | endif

set laststatus=2
set statusline=
set statusline+=%f\ [FORMAT=%{&ff}]
set statusline+=%m\ [TYPE=%Y]
set statusline+=%r\ [POS=%l,%v]
set statusline+=\ \ \ \ \ \GIT_branch= 
let gitBranch=system('git rev-parse --abbrev-ref HEAD')
exe "set statusline+=" . gitBranch 

set foldmethod=indent   " fold based on indent

"curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

" show hidden files
let NERDTreeShowHidden=1

let g:NERDTreeWinSize = 18
autocmd VimEnter * NERDTree | wincmd p

autocmd BufEnter NERD_tree_* | execute 'normal R'
au CursorHold * if exists("t:NerdTreeBufName") | call <SNR>15_refreshRoot() | endif

augroup DIRCHANGE
    au!
    autocmd DirChanged global :NERDTreeCWD
augroup END

autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

call plug#begin()
Plug 'preservim/NERDTree' "Чтобы открыть окно с деревом файлов, вводим команду : NERDTree:
call plug#end() " :PlugInstall

let g:NERDTreeMinimalMenu=1
let g:NERDTreeDirArrows=0
set encoding=utf-8
